<template>
  <TopBar />
  <div class="relative bg-blue-400 z-0 dark:bg-gray-700 dark:text-white">
    <div class="flex flex-col items-center h-screen justify-center gap-y-5">
      <h1 class="text-2xl font-sans">NAVO</h1>
      <div class="flex bg-white w-[50%] rounded-lg relative">
        <input
          type="search"
          class="w-[90%] rounded-lg py-4 px-2 focus:"
          placeholder="What you are looking for?"
          name=""
          id=""
        />
        <button class="flex items-center absolute right-4 top-2">
          <span class="material-symbols-outlined text-black text-4xl">
            search
          </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import TopBar from "@/components/TopBar.vue";
export default {
  name: "HomeView",
  components: {
    TopBar,
  },
};
</script>
