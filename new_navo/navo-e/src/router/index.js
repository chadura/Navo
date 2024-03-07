import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ListPage from "../views/ListPage.vue";
import SettingsView from "@/views/SettingsView.vue";
import ProfileLogin from "../components/ProfileLogin.vue";

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
    path: "/list-page",
    name: "ListPage",
    component: ListPage,
  },
  { path: "/profile-login", name: "LoginProfile", component: ProfileLogin },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
