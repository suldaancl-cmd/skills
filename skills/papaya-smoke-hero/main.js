// Papaya Smoke Hero — entrance choreography
// Stack: GSAP 3.12 + ScrollTrigger + SplitType 0.3 + Lenis 1.0
// All libraries loaded from CDN in template.html before this file.

window.addEventListener('load', () => {
  if (window.gsap && window.ScrollTrigger) gsap.registerPlugin(ScrollTrigger);

  // ----- smooth scroll -----
  let lenis = null;
  if (window.Lenis) {
    lenis = new Lenis({
      duration: 1.1,
      easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
    });
    if (window.gsap) {
      lenis.on('scroll', () => ScrollTrigger.update());
      gsap.ticker.add(t => lenis.raf(t * 1000));
      gsap.ticker.lagSmoothing(0);
    }
  }

  // ----- split headline into words, then wrap each word in a div for clip-mask -----
  const headline = document.querySelector('.display');
  if (headline && window.SplitType) {
    new SplitType(headline, { types: 'words' });
    headline.querySelectorAll('.word').forEach(w => {
      const inner = document.createElement('div');
      inner.innerHTML = w.innerHTML;
      w.innerHTML = '';
      w.appendChild(inner);
    });
  }

  // ----- intro timeline -----
  const tl = gsap.timeline({ defaults: { ease: 'expo.out' } });
  tl.from('.hud',         { y: -20, opacity: 0, duration: 0.6 }, 0)
    .from('.eyebrow',     { y: 20, opacity: 0, duration: 0.7, delay: 0.15 }, 0)
    .from('.display .word > div', { yPercent: 110, duration: 1.0, stagger: 0.05 }, '-=0.4')
    .from('.accent-line', { scaleX: 0, duration: 1.1 }, '-=0.5')
    .from('.lede',        { y: 24, opacity: 0, duration: 0.8 }, '-=0.7')
    .from('.cta',         { y: 24, opacity: 0, duration: 0.7 }, '-=0.5');

  // ----- HUD telemetry counter -----
  const counter = document.querySelector('[data-counter]');
  if (counter) {
    const obj = { v: 0 };
    gsap.to(obj, {
      v: 12,
      duration: 2.2,
      ease: 'power2.out',
      delay: 0.6,
      onUpdate: () => {
        counter.textContent = String(Math.round(obj.v)).padStart(2, '0');
      },
    });
  }

  // ----- pin + fade hero on scroll -----
  if (window.ScrollTrigger) {
    gsap.to('.hero-inner', {
      opacity: 0,
      y: -60,
      ease: 'none',
      scrollTrigger: {
        trigger: '.hero',
        start: 'top top',
        end: 'bottom 30%',
        scrub: 1,
      },
    });
  }

  // ----- auto-seed smoke so the page isn't dead before the user moves -----
  // Dispatches synthetic mousemoves on the canvas for ~3s after load,
  // tracing a slow figure-8 so the smoke shader paints visible plumes.
  const c = document.querySelector('#smoke canvas');
  if (c) {
    const r = c.getBoundingClientRect();
    let i = 0;
    const totalFrames = 180;
    const tick = () => {
      if (i >= totalFrames) return;
      const t = i / totalFrames;
      const x = r.left + r.width  * (0.5 + 0.32 * Math.sin(t * Math.PI * 4));
      const y = r.top  + r.height * (0.5 + 0.28 * Math.cos(t * Math.PI * 2));
      c.dispatchEvent(new MouseEvent('mousemove', { bubbles: true, clientX: x, clientY: y }));
      i++;
      requestAnimationFrame(tick);
    };
    setTimeout(tick, 600);
  }

  // ----- respect prefers-reduced-motion -----
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    tl.progress(1);
    if (lenis) lenis.destroy();
  }
});
