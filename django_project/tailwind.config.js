/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
	  './messaging/templates/messaging/*.html',
  ],
  theme: {
    extend: {
		colors: {
			'twitter-blue': '#1DA1F2',
		},
	},
  },
  plugins: [],
}

