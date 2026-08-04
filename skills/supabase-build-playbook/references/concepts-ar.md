# مفاهيم Supabase — النسخة المصحّحة (عربي)

هذا هو الأساس النظري قبل البناء. الترتيب هو نفسه ترتيب التعلّم الصحيح. تحت كل
مفهوم سطر أو سطران للشرح، ومربّع **⚠ عمق** فقط حيث يوجد شيء يتجاوز الشرح الشائع
ويعضّك وقت التنفيذ. كل الأكواد LTR كما هي.

> القاعدة الذهبية: لا تبنِ أي `table` بدون `RLS`، ولا تضع `service_role` /
> `secret key` في الـ frontend، ولا تبدأ CRM بدون `company_id` / `user_id` /
> `role`.

---

## 1. Database — قاعدة البيانات
Supabase هو **PostgreSQL كامل** لكل مشروع، مع backups وextensions وReatime فوقه.
كل شيء بعد ذلك مجرّد إضافات على Postgres.

## 2. Tables / Rows / Columns
الجدول = نوع كيان واحد. الصف = سجل واحد. العمود = صفة. الفكرة الأهم (وردت في
الفيديو): **كل جدول يمثّل كياناً واحداً فقط** — جدول `products` يفكّر بالمنتجات
فقط، لا بالطلبات ولا بالعملاء.

## 3. Auth — المستخدمون
نظام تسجيل دخول جاهز: email/password، magic link، OAuth (Google…). يعطي كل مستخدم
`user_id` (في جدول `auth.users`) تربط به بياناته.

> **⚠ عمق:** في Next.js لا تستخدم عميلاً واحداً. النمط الحديث = حزمتان
> (`@supabase/supabase-js` + `@supabase/ssr`) وعميلان منفصلان (browser/server)
> + `middleware` لتجديد الجلسة. التفاصيل في `nextjs-ssr-auth.md`.

## 4. RLS — Row Level Security
يحدّد **من يرى/يعدّل أي صف**. يجب أن يكون مفعّلاً على كل جدول في schema مكشوف مثل
`public`. جدول بدون RLS + publishable key في المتصفح = قاعدتك مكشوفة للجميع.

> **⚠ عمق:** فعّله فوراً بعد إنشاء الجدول: `alter table x enable row level
> security;`. مع RLS وبدون policies الجدول مقفل للجميع (default-deny) — تفتح
> الوصول بسياسة واحدة لكل عملية.

## 5. Policies — القوانين
RLS هو النظام، الـ Policies هي القواعد. كل policy تضيف شرطاً تلقائياً على الـ query.

> **⚠ عمق (أهم تصحيح):** «policy = شرط `WHERE`» صحيح للقراءة فقط.
> - `SELECT` / `DELETE` → `USING`
> - `INSERT` → `WITH CHECK` فقط (لا يوجد صف قديم ليُفلتر)
> - `UPDATE` → الاثنان معاً
>
> نسيان `WITH CHECK` على `INSERT` = الخطأ الشهير
> `new row violates row-level security policy`. والأمثلة في `rls-cookbook.md`.

## 6. API تلقائي
كل جدول يعطيك REST + GraphQL جاهزاً. تستعمل الـ client مباشرة:
```js
const { data } = await supabase.from("clients").select("*")
```
لكن الحماية الحقيقية ليست في الـ API بل في الـ policies — الـ API يحترم RLS.

## 7. anon / service_role (والأسماء الجديدة 2025)
- `publishable` (سابقاً `anon`): للـ frontend، آمن، محكوم بـ RLS.
- `secret` (سابقاً `service_role`): للـ backend فقط.

> **⚠ عمق:** `secret`/`service_role` لا «يتجاوز الحماية» فحسب — هو **يلغي RLS
> تماماً** ويرى ويكتب كل صف. لو وصل المتصفح أو أي متغيّر `NEXT_PUBLIC_*` /
> `VITE_*` اعتبره مسرّباً وغيّره فوراً. الأسماء الجديدة: `sb_publishable_...` /
> `sb_secret_...`.

## 8. Storage — تخزين الملفات
للصور/الفيديو/PDF/ملفات العملاء. مرتبط بقاعدة البيانات ويُحمى بـ RLS.

> **⚠ عمق:** اجعل الـ bucket خاصاً (Public OFF)، رتّب الملفات
> `{auth.uid()}/{filename}`، وقدّم الملفات عبر `createSignedUrl(path, seconds)`
> لا روابط خام. bucket عام لبيانات المستخدمين = الرابط مكشوف للأبد.

## 9. Realtime — التحديث المباشر
استمع لتغييرات قاعدة البيانات وادفعها للواجهة بلا refresh (رسالة جديدة، تغيّر
حالة طلب، notification). يحترم RLS أيضاً.

## 10. Edge Functions
دوال TypeScript تعمل على السيرفر للأشياء الحساسة: Stripe webhook، إرسال إيميل،
استدعاء AI بمفتاح خاص، إجراءات الأدمن. أي شيء لا يصح أن يكون في الـ frontend.

## 11. Database Webhooks
عند تغيّر صف (`INSERT`/`UPDATE`/`DELETE`) أرسل حدثاً لنظام آخر (lead جديد →
WhatsApp، `paid` → فاتورة).

## 12. Migrations
عند الجدّية توقّف عن تعديل الجداول يدوياً من الـ Dashboard. احفظ التغييرات كملفات
migration قابلة للمراجعة والإعادة (مهم مع Claude Code / git / الفريق).

## 13. Relationships
`foreign keys` تربط الجداول: `1:1`، `1:many` (عميل ← عدة مشاريع)، `many:many`
(عبر join table). مثال الفيديو: دولة ↔ عملة (`1:1`).

> **⚠ عمق:** Postgres لا يفهرس الـ FK تلقائياً. أي عمود يربط أو تفلتر عليه policy
> (`user_id`, `company_id`) لازم عليه `index`، وإلا كل query محمي = sequential
> scan.

## 14. Roles — الصلاحيات
`owner` / `admin` / `member` / `viewer`. تُخزَّن عادة في جدول `profiles`
(`id`, `user_id`, `full_name`, `role`, `company_id`).

> **⚠ عمق:** اقرأ الدور عبر دالة `security definer` (مثل `current_role()`) لا عبر
> subquery داخل الـ policy — لتفادي الـ recursion. انظر المفهوم 15.

## 15. Multi-tenant — الأهم لـ DashboardOS / CRM
نظام واحد يخدم عدة شركات، كل شركة ترى بياناتها فقط. أضِف في كل جدول مهم:
`company_id` + `created_by` + `created_at`.

> **⚠ عمق (أصعب جزء):** سياسة على جدول `projects` فيها subquery يرجع لجدول RLS
> يرجّعك له → `infinite recursion detected in policy`. الحل: اقرأ الـ tenancy عبر
> دالة `security definer` بـ `search_path` مقفل (`current_company_id()`)، لا عبر
> subquery مباشر. السكيمة الجاهزة كاملة في `multitenant-starter.sql`.

---

## ترتيب التعلّم/البناء
1. Tables / Rows / Columns + علاقات
2. تفعيل RLS على كل جدول
3. Policies (انتبه `USING` مقابل `WITH CHECK`)
4. الفهارس على أعمدة RLS و FK
5. Auth (في Next.js: نمط `@supabase/ssr`)
6. Storage (bucket خاص + signed URLs)
7. Edge Functions للمنطق الحساس
8. Migrations عند الجدّية

## أهم 5 مفاهيم لو الهدف WebsiteOS / Dashboard / CMS / CRM
`PostgreSQL tables` ← `Auth users` ← `RLS policies` ← `Relationships` ←
`Edge Functions` للمنطق الآمن.
