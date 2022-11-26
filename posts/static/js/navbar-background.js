export const setBackground = () => {
    const navbarButton = document.querySelector('.navbar-toggler');
    
    // const prefersDarkTheme = window.matchMedia('(prefers-color-scheme: dark)');
  
    let currentTheme;
    if (localStorage.getItem('theme')) {
      currentTheme = localStorage.getItem('theme');
    } else {
      if (prefersDarkTheme.matches) {
        localStorage.setItem('theme', 'dark');
      } else {
        localStorage.setItem('theme', 'light');
        currentTheme = localStorage.getItem('theme');
      }
    }
    
    let expanded = navbarButton.getAttribute('aria-expanded');
    let first = true;
    toggleBackground(expanded);
    navbarButton.addEventListener('click', function () {
      expanded = navbarButton.getAttribute('aria-expanded')
      toggleBackground(expanded);
    });
  
    function toggleBackground(expanded) {
      if (expanded == 'true') {
        $('.navbar.bg-dark').css("--bs-bg-opacity", "1");
        if (!first) {
            $('.navbar.bg-dark').css("transition-duration", "1000ms");
        }
      } else {
        $('.navbar.bg-dark').css("--bs-bg-opacity", "0");
        if (!first) {
            $('.navbar.bg-dark').css("transition-duration", "1000ms");
        }
      }
      first = false;
    }
  }
  
  export default {
    setBackground,
  }