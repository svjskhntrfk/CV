function detectUserTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        return savedTheme;
    }

    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        return 'dark-theme';
    }

    const hour = new Date().getHours();
    return (hour > 18 || hour < 6) ? 'dark-theme' : 'light-theme';
}

document.addEventListener('DOMContentLoaded', () => {
    const theme = detectUserTheme();
    
    fetch('/set_theme', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ theme: theme })
    });
});
