export const setTheme = () => {
  const themeBtn = document.querySelector('.theme-toggler');
  const prefersDarkTheme = window.matchMedia('(prefers-color-scheme: dark)');

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

  if (currentTheme == 'dark') {
    // set dark theme
    document.body.setAttribute('data-theme', 'dark');
    themeBtn.innerHTML = '<i class="far fa-sun" aria-hidden="true"> Jour</i>';
  } else {
    // set light theme
    document.body.setAttribute('data-theme', 'light');
    themeBtn.innerHTML = '<i class="far fa-moon" aria-hidden="true"> Nuit</i>';
  }

  themeBtn.addEventListener('click', function () {
    const theme = document.body.getAttribute('data-theme');

    toggleTheme(theme);
  });

  function toggleTheme(theme) {
    if (theme == 'dark') {
      document.body.setAttribute('data-theme', 'light');
      themeBtn.innerHTML = '<i class="far fa-moon" aria-hidden="true"> Nuit</i>';
      localStorage.setItem('theme', 'light');
    } else {
      document.body.setAttribute('data-theme', 'dark');
      themeBtn.innerHTML = '<i class="far fa-sun" aria-hidden="true"> Jour</i>';
      localStorage.setItem('theme', 'dark');
    }
  }
}

export default {
  setTheme,
}