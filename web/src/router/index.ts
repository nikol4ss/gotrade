import { createRouter, createWebHistory } from "vue-router"

import Layout from "@/pages/Layout.vue"
import Dashboard from "@/pages/Dashboard.vue"

import CryptoMarket from "@/pages/Crypto/CryptoMarket.vue"

const routes = [
  {
    path: "/",
    component: Layout,
    children: [
      { path: "dashboad", component: Dashboard, meta: { breadcrumb: "Dashboard" } },
      { path: "crypto/market", component: CryptoMarket, meta: { breadcrumb: ["Crypto", "Market"] } },
    ],
  },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
