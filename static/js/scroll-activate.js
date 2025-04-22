document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.getElementById('menuToggle');
  const topNav     = document.getElementById('topNav');
  const slides     = Array.from(document.querySelectorAll('.section-slide'));

  // 1) If ?slide=N is present and valid, jump there immediately:
  const params = new URLSearchParams(window.location.search);
  const target = parseInt(params.get('slide'), 10);
  if (!isNaN(target) && target >= 0 && target < slides.length) {
    slides[target].scrollIntoView({ behavior: 'auto', block: 'start' });
  }

  // 2) On scroll, find which slide is centered and expand/collapse:
  function updateMenu() {
    const scrollY = window.scrollY;
    const midPoint = window.innerHeight / 2;
    let current = 0;

    for (let i = 0; i < slides.length; i++) {
      if (scrollY + midPoint >= slides[i].offsetTop) {
        current = i;
      }
    }

    if (current === 0) {
      menuToggle.classList.add('active');
      topNav.classList.add('open');
    } else {
      menuToggle.classList.remove('active');
      topNav.classList.remove('open');
    }
  }

  window.addEventListener('scroll', updateMenu);
  updateMenu();  // initial state
});
