// Elementos que aparecerán con animación
const elementos = document.querySelectorAll('.proyectos h2, .project-card');

// Respetamos a quien pidió menos movimiento en su sistema
const menosMovimiento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!menosMovimiento && 'IntersectionObserver' in window) {
    // Los ocultamos desde JS: si JS falla, el contenido se ve igual
    elementos.forEach((el) => el.classList.add('reveal'));

    const observador = new IntersectionObserver((entradas) => {
        entradas
            .filter((entrada) => entrada.isIntersecting)
            .forEach((entrada, i) => {
                // Los que entran juntos aparecen uno tras otro (0.12s de diferencia)
                entrada.target.style.setProperty('--retraso', `${i * 0.12}s`);
                entrada.target.classList.add('visible');
                observador.unobserve(entrada.target); // anima una sola vez
            });
    }, { threshold: 0.2 });

    elementos.forEach((el) => observador.observe(el));
}