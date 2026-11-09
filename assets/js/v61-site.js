// Original v6.1 reveal and typewriter behavior, adapted to work across Jekyll pages.
(() => {
  const revealEls = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    const obs = new IntersectionObserver(e => {
      e.forEach(x => { if (x.isIntersecting) { x.target.classList.add('on'); obs.unobserve(x.target); } });
    }, { threshold: .1, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(el => obs.observe(el));
  } else revealEls.forEach(el => el.classList.add('on'));

  const tw = document.getElementById('typewriter');
  const coldOpen = document.querySelector('.cold-open');
  if (tw && coldOpen) {
    const text = tw.getAttribute('data-text') || 'The road into Svaneti is not a road. It is a dare.';
    let i = 0;
    function type() {
      if (i <= text.length) {
        tw.textContent = text.slice(0, i);
        const caret = document.createElement('span'); caret.className='caret'; tw.appendChild(caret);
        const ch = text[i - 1];
        const delay = ch === '.' || ch === ',' ? 260 : (Math.random() * 45 + 38);
        i++; setTimeout(type, delay);
      }
    }
    if ('IntersectionObserver' in window) {
      const coObs = new IntersectionObserver(e => {
        e.forEach(x => { if (x.isIntersecting) { type(); coObs.disconnect(); } });
      }, { threshold: .4 });
      coObs.observe(coldOpen);
    } else type();
  }

  // Prevent false subscription confirmations: the prototype has no mailing-list backend.
  const form=document.querySelector('.sub-form');
  if (form) form.addEventListener('submit', e => {
    e.preventDefault();
    const message=document.getElementById('sor-signup-message');
    if (message) message.textContent='Subscriptions are not yet active.';
  });
})();
