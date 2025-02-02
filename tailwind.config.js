// tailwind.config.js
export default {
    content: [
      './index.html',
      './src/**/*.{js,ts,jsx,tsx}', // Ensure Tailwind purges unused styles
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  };
  