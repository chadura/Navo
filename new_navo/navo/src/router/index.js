import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ListPage from "../views/ListPage.vue";
import SettingsView from "@/views/SettingsView.vue";
import BlogPage from "@/components/BlogPage.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/settings",
    name: "SettingsView",
    component: SettingsView,
  },
  {
    path: "/list",
    name: "ListPage",
    component: ListPage,
  },
  {
    path: "/new",
    name: "BlogPage",
    component: BlogPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
