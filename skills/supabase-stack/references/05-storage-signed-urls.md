# 05 — Private storage with signed URLs

Files live in a **private** bucket. The DB only stores the path. The frontend asks Supabase to mint a short-lived signed URL each time it needs to show the file.

## Layout

- Bucket name: `app-files` (default — keep it for the policy script to match)
- Object key: `{auth.uid()}/{filename}` — one folder per user
- Bucket public toggle: **OFF**

## The storage RLS policies (run once after creating the bucket)

```sql
-- Allow each user to SELECT only their own folder
create policy "app_files_select_own"
  on storage.objects for select
  using (
    bucket_id = 'app-files'
    and auth.uid()::text = (storage.foldername(name))[1]
  );

-- Allow each user to INSERT only into their own folder
create policy "app_files_insert_own"
  on storage.objects for insert
  with check (
    bucket_id = 'app-files'
    and auth.uid()::text = (storage.foldername(name))[1]
  );

-- Allow UPDATE only on own objects
create policy "app_files_update_own"
  on storage.objects for update
  using (
    bucket_id = 'app-files'
    and auth.uid()::text = (storage.foldername(name))[1]
  );

-- Allow DELETE only on own objects
create policy "app_files_delete_own"
  on storage.objects for delete
  using (
    bucket_id = 'app-files'
    and auth.uid()::text = (storage.foldername(name))[1]
  );
```

**If you renamed the bucket, change `'app-files'` in all four policies.** This is the silent-failure landmine Profit Studio warns about.

## Upload / fetch / delete in the frontend

```js
import { supabase } from "./supabaseClient";

async function uploadUserFile(file) {
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) throw new Error("not signed in");

  const path = `${user.id}/${Date.now()}_${file.name}`;
  const { error } = await supabase.storage
    .from("app-files")
    .upload(path, file, { cacheControl: "3600", upsert: false });
  if (error) throw error;

  // Save the path in your DB row so you can render it later.
  return path;
}

async function getSignedUrlFor(path, expiresInSeconds = 60 * 10) {
  const { data, error } = await supabase.storage
    .from("app-files")
    .createSignedUrl(path, expiresInSeconds);
  if (error) throw error;
  return data.signedUrl;  // good for `expiresInSeconds` seconds
}

async function deleteUserFile(path) {
  const { error } = await supabase.storage.from("app-files").remove([path]);
  if (error) throw error;
}
```

## Paste-ready prompt

```text
Connect the existing file-upload UI in this project to Supabase Storage.

Use the Supabase client from: src/supabaseClient.js
Use the existing bucket named "app-files" (private).

1) When the user picks files to upload:
   - For each file, build the path as `${user.id}/${Date.now()}_${file.name}`.
     Get `user` via `supabase.auth.getUser()`.
   - Call `supabase.storage.from("app-files").upload(path, file)`.
   - Save the resulting path inside the related row in the database
     (column: `attachments` as a `text[]`, append the path).

2) When rendering an uploaded file:
   - The bucket is PRIVATE, so do NOT use a public URL.
   - Call `supabase.storage.from("app-files").createSignedUrl(path, 600)`
     and use `data.signedUrl` as the `src`.

3) When the user deletes a file from the app:
   - Remove it from storage with `storage.from("app-files").remove([path])`.
   - Also remove the path from the database row.

4) Do not change the UI/UX. Just add the logic.

Show me only the files you changed.
```

## Manual steps (Supabase dashboard)

1. **Storage → New bucket**.
2. **Name**: `app-files`.
3. **Public bucket**: **OFF**.
4. Create.
5. **SQL Editor** → paste the four policies above → Run.
6. (Optional) **Storage → app-files → Policies** tab → verify all four show up.

## Why signed URLs and not public

A public bucket gives every uploaded file a forever-valid URL. If one URL leaks (DM, screenshot, browser history sync) the file is exposed permanently. A signed URL expires — by default in this skill, 10 minutes. The frontend re-signs on demand, which is cheap.

For files that genuinely should be public (e.g. user avatars), spin up a separate `public` bucket and pin the policies there. Don't mix public and private files in one bucket.

## Common pitfalls

- **`new row violates row-level security policy`** on upload → the policy `bucket_id` string doesn't match the bucket name you actually created.
- **Files upload but render broken** → you used `getPublicUrl` on a private bucket. Switch to `createSignedUrl`.
- **Signed URL `403`s after a refresh** → it expired. Re-sign on every render; don't cache for longer than the TTL.
- **Image preview flashes a stale signed URL after re-upload** → the path stayed the same, but the file changed. Either rename the path on upload (the `Date.now()_` prefix above handles this), or pass `cacheBust=true`-style query param.
