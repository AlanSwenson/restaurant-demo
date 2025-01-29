document.addEventListener('DOMContentLoaded', () => {
  const returnToTop = document.getElementById('return-to-top');
  
  window.addEventListener('scroll', () => {
    if (window.scrollY >= 50) {
      returnToTop?.classList.remove('hidden');
    } else {
      returnToTop?.classList.add('hidden');
    }
  });

  returnToTop?.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}); 