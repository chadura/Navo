<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import TopBar from "./components/TopBar.vue";
import settings from "./components/settings/Settings.vue";
</script>

<template>
  <div class="relative h-screen bg z-0">
    <TopBar />

    <button
      @click="isOpen"
      class="material-symbols-outlined fixed text-gray-200 right-6 top-24"
    >
      settings
    </button>

    <div
      class="absolute w-full top-0 h-full flex flex-col items-center justify-center gap-y-10"
    >
      <div class="flex flex-col lg:flex-row items-center gap-1">
        <img src="../src/assets/navo-icon.png" class="w-[100px] h-[100px]" />
        <h1 class="font-bold text-xl lg:text-xl text-gray-200">Navo</h1>
      </div>
      <div class="flex bg-white lg:w-[30%] relative rounded-lg">
        <input
          type="text"
          class="outline-none font-bold w-[90%] py-4 px-2 rounded-lg"
          placeholder="What you are looking for?"
          name=""
          id=""
        />
        <button
          class="flex items-center justify-center absolute right-4 h-full"
        >
          <span class="material-symbols-outlined text-gray-600 text-2xl">
            search
          </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import TopBar from "./components/TopBar.vue";
export default {
  name: "HomeView",
  components: {
    TopBar,
    settings,
  },
};
</script>

<style scoped>
.bg {
  background-color: #4c119b;
  background-image: linear-gradient(
    121.55deg,
    #0f82d3 17.34%,
    #253a1f 113.19%
  ) !important;
}
</style>

