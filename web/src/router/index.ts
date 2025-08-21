import { createMemoryHistory, createRouter } from 'vue-router'

import Dashboard from '../pages/dashboard/Dashboard.vue'


const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/dashboard', component: Dashboard },
]

export const router = createRouter({
  history: createMemoryHistory(),
  routes,
})
