// ── Mobile hamburger menu ──────────────────────────
const hamburger = document.getElementById('hamburger');
const navList   = document.getElementById('nav-list');

if (hamburger && navList) {
  hamburger.addEventListener('click', () => {
    navList.classList.toggle('open');
  });
  // Close nav when clicking outside
  document.addEventListener('click', (e) => {
    if (!hamburger.contains(e.target) && !navList.contains(e.target)) {
      navList.classList.remove('open');
    }
  });
}

// ── Sticky header shadow ──────────────────────────
window.addEventListener('scroll', () => {
  const header = document.getElementById('site-header');
  if (header) {
    header.style.boxShadow = window.scrollY > 10
      ? '0 4px 20px rgba(0,0,0,.12)'
      : '0 2px 8px rgba(0,0,0,.06)';
  }
});

// ── Image lazy-load fallback ──────────────────────
document.querySelectorAll('img').forEach(img => {
  img.addEventListener('error', () => {
    img.style.display = 'none';
    const parent = img.parentElement;
    if (parent && !parent.querySelector('.no-img')) {
      parent.innerHTML = '<div class="no-img"><i class="fa fa-newspaper"></i></div>';
    }
  });
});
