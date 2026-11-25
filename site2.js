{
const h = document.querySelector('header');
const hero = document.querySelector('.hero');
const sc = () => h.classList.toggle('solid', !hero || scrollY > 40);
sc(); addEventListener('scroll', sc, {passive: true});
const R = matchMedia('(prefers-reduced-motion: reduce)').matches;
const io = ('IntersectionObserver' in window) ? new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('on'); io.unobserve(e.target); }
}), {threshold: .12}) : null;
document.documentElement.classList.add('js');
document.querySelectorAll('.rv,.steps').forEach(el => {
  if (!io || R) { el.classList.add('on'); return; }
  el.style.transitionDelay = (el.dataset.d || 0) + 'ms';
  io.observe(el);
});
let w = document.querySelector('.hero h1 span');
if (w && !R) {
  const L = JSON.parse(w.dataset.w); let k = 0;
  setInterval(() => {
    k = (k + 1) % L.length;
    const n = w.cloneNode(); n.textContent = L[k]; w.replaceWith(n); w = n;
  }, 3200);
}
}

/* menu Connexion déroulant */
(()=>{const b=document.getElementById('cxB'),p=document.getElementById('cxP');if(!b||!p)return;
  const set=o=>{p.classList.toggle('open',o);b.setAttribute('aria-expanded',o);document.querySelector('header')?.classList.toggle('cxo',o)};
  b.addEventListener('click',e=>{e.stopPropagation();set(!p.classList.contains('open'))});
  document.addEventListener('click',e=>{if(!p.contains(e.target))set(false)});document.addEventListener('keydown',e=>{if(e.key==='Escape'){set(false);b.focus()}})})();
