import { createRouter, createWebHashHistory } from 'vue-router'
import SolveView from '../views/SolveView.vue'
import VerifyView from '../views/VerifyView.vue'

export const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', redirect: '/solve' },
    { path: '/solve', component: SolveView },
    { path: '/verify', component: VerifyView },
  ],
})
