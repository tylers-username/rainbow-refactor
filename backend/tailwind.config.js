/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./upsun_demo_app/templates/**/*.html",
    "./upsun_demo_app/static/**/*.js",
  ],
  theme: {
    extend: {
      fontSize: {
        15: "0.9375rem", // 15px
      },
      textColor: {
        default: "var(--upsun-colors-neutral-light-white, #FFF)",
      },
      colors: {
        "upsun-black-900": "var(--upsun-colors-black-900)",
        "upsun-black-800": "var(--upsun-colors-black-800)",
        "upsun-violet-600": "var(--upsun-colors-violet-600)",
        "upsun-violet-900": "var(--upsun-colors-violet-900)",
        "upsun-yellow-400": "var(--upsun-colors-yellow-400)",
      },
      fontFamily: {
        "sans-strong": [
          "Space Grotesk",
          "system-ui",
          "-apple-system",
          "BlinkMacSystemFont",
          "Segoe UI",
          "Roboto",
          "Helvetica Neue",
          "Arial",
          "sans-serif",
        ],
        "sans-soft": ["Open Sans", "sans-serif"],
        mono: ['"Overpass Mono"', "monospace"],
      },
    },
  },
  plugins: [],
};
