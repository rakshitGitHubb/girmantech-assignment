import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Import Tailwind + custom styles
import './style.css'

const app = createApp(App)
app.use(router)
app.mount('#app')
