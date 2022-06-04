const themeBtn = document.querySelector('.theme-toggler');
const prefersDarkTheme = window.matchMedia('(prefers-color-scheme: dark)');

if (prefersDarkTheme.matches) {
  localStorage.setItem('theme', 'dark');
}

const currentTheme = localStorage.getItem('theme');

if (currentTheme == 'dark') {
  // set dark theme
  document.body.setAttribute('data-theme', 'dark');
  themeBtn.innerHTML = '<i class="fa fa-sun-o" aria-hidden="true"></i>';
} else {
  // set light theme
  document.body.setAttribute('data-theme', 'light');
  themeBtn.innerHTML = '<i class="fa fa-moon-o" aria-hidden="true"></i>';
}

themeBtn.addEventListener('click', function () {
  const theme = document.body.getAttribute('data-theme');

  toggleTheme(theme);
});

function toggleTheme(theme) {
  if (theme == 'dark') {
    document.body.setAttribute('data-theme', 'light');
    themeBtn.innerHTML = '<i class="fa fa-moon-o" aria-hidden="true"></i>';
    localStorage.setItem('theme', 'light');
  } else {
    document.body.setAttribute('data-theme', 'dark');
    themeBtn.innerHTML = '<i class="fa fa-sun-o" aria-hidden="true"></i>';
    localStorage.setItem('theme', 'dark');
  }
}
