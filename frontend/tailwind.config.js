/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}','./src/app.html'],
  theme: {
    extend: {
      fontFamily:{
          'brand': ['"Inter"', 'sans-serif'],
          'header': ['"Inter"', 'sans-serif'],
          'nav': ['"Inter"', 'sans-serif'],
      },
      transitionProperty: {
        'height': 'height',
        'spacing': 'margin, padding',
      },
      typography: {
        DEFAULT: {
          css: {
            marginBottom: '0'
          }
        }
      }
    },
    
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

