// ============================================
//   ISPRMM Portal Académico - Lógica principal
// ============================================

// --- Configuración de Tailwind ---
tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            "colors": {
                "on-tertiary": "#ffffff",
                "outline-variant": "#c3c5d7",
                "inverse-on-surface": "#ebf1ff",
                "on-error": "#ffffff",
                "surface-container": "#e7eefe",
                "surface-container-highest": "#dce2f3",
                "on-secondary-fixed-variant": "#5a00c6",
                "on-primary-fixed": "#00174d",
                "inverse-primary": "#b5c4ff",
                "surface-bright": "#f9f9ff",
                "secondary-container": "#8b4aff",
                "inverse-surface": "#2a313d",
                "tertiary": "#005438",
                "on-secondary-container": "#fffbff",
                "tertiary-fixed-dim": "#63dca6",
                "on-primary-fixed-variant": "#003dab",
                "primary-fixed-dim": "#b5c4ff",
                "surface": "#f9f9ff",
                "tertiary-container": "#006f4b",
                "on-secondary": "#ffffff",
                "secondary-fixed": "#eaddff",
                "background": "#f9f9ff",
                "on-tertiary-container": "#7af3bb",
                "secondary-fixed-dim": "#d2bbff",
                "primary": "#003fb1",
                "on-primary-container": "#d4dcff",
                "on-tertiary-fixed": "#002113",
                "on-background": "#151c27",
                "primary-fixed": "#dbe1ff",
                "on-secondary-fixed": "#25005a",
                "on-surface-variant": "#434654",
                "on-primary": "#ffffff",
                "surface-tint": "#1353d8",
                "tertiary-fixed": "#81f9c1",
                "secondary": "#7127e5",
                "surface-container-high": "#e2e8f8",
                "primary-container": "#1a56db",
                "on-surface": "#151c27",
                "on-tertiary-fixed-variant": "#005236",
                "error-container": "#ffdad6",
                "surface-container-lowest": "#ffffff",
                "error": "#ba1a1a",
                "on-error-container": "#93000a",
                "surface-variant": "#dce2f3",
                "surface-container-low": "#f0f3ff",
                "outline": "#737686",
                "surface-dim": "#d3daea"
            },
            "borderRadius": {
                "DEFAULT": "0.25rem",
                "lg": "0.5rem",
                "xl": "0.75rem",
                "full": "9999px"
            },
            "spacing": {
                "xs": "4px",
                "lg": "24px",
                "base": "4px",
                "gutter": "24px",
                "md": "16px",
                "sm": "8px",
                "xl": "32px",
                "container-margin-mobile": "16px",
                "container-margin-desktop": "40px"
            },
            "fontFamily": {
                "display-lg": ["Inter"],
                "body-md": ["Inter"],
                "label-sm": ["Inter"],
                "headline-md": ["Inter"],
                "label-md": ["Inter"],
                "headline-sm": ["Inter"],
                "body-sm": ["Inter"],
                "body-lg": ["Inter"]
            },
            "fontSize": {
                "display-lg": ["36px", { "lineHeight": "44px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }],
                "label-sm": ["11px", { "lineHeight": "14px", "fontWeight": "500" }],
                "headline-md": ["24px", { "lineHeight": "32px", "fontWeight": "600" }],
                "label-md": ["12px", { "lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600" }],
                "headline-sm": ["20px", { "lineHeight": "28px", "fontWeight": "600" }],
                "body-sm": ["14px", { "lineHeight": "20px", "fontWeight": "400" }],
                "body-lg": ["18px", { "lineHeight": "28px", "fontWeight": "400" }]
            }
        }
    }
};

// --- Interacción del sidebar en móvil ---
document.querySelector('header button').addEventListener('click', () => {
    const sidebar = document.querySelector('aside');
    sidebar.classList.toggle('hidden');
    sidebar.classList.toggle('fixed');
    sidebar.classList.toggle('inset-0');
    sidebar.classList.toggle('bg-black/20');
});

// --- Efecto de elevación tonal en tarjetas ---
document.querySelectorAll('.bg-surface-container-lowest').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-2px)';
        card.classList.add('shadow-md');
        card.style.transition = 'all 0.3s ease';
    });
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0)';
        card.classList.remove('shadow-md');
    });
});