<template>
  <div
    class="flex bg-gray-600 p-1 gap-x-10 justify-between dark:bg-white dark:text-black relative z-50"
  >
    <div class="flex items-center gap-x-3">
      <span
        class="text-left material-symbols-outlined text-lg text-gray-200 dark:text-black"
      >
        arrow_back
      </span>
      <span
        class="text-left material-symbols-outlined text-lg text-gray-200 dark:text-black"
      >
        arrow_forward
      </span>
      <span
        class="text-left material-symbols-outlined text-gray-200 dark:text-black text-lg"
      >
        refresh
      </span>
    </div>

    <!-- Search Bar -->
    <div
      class="flex w-[400px] relative border z-50 justify-center items-center bg-white dark:text-black rounded-lg"
    >
      <input type="text" placeholder="Search" class="py-3 w-[350px] outline-none" />
      <span class="material-symbols-outlined absolute right-0 cursor-pointer"
        >Search</span
      >
    </div>

    <div class="flex items-center gap-x-3">
      <button>
        <span
          class="text-left material-symbols-outlined text-white dark:text-black text-lg"
        >
          bookmarks
        </span>
      </button>

      <h2>
        <span
          class="text-left material-symbols-outlined text-white dark:text-black text-lg"
        >
          account_circle
        </span>
      </h2>
      <button>
        <span
          class="text-left material-symbols-outlined text-white dark:text-black text-lg"
        >
          extension
        </span>
      </button>
      <button @click="toggleMenu" ref="dropdown">
        <span
          class="text-left material-symbols-outlined text-white dark:text-black text-lg"
        >
          menu
        </span>
      </button>
    </div>
  </div>
  <div
    v-if="isMenuOpen"
    class="shadow-md lg:w-[35%] xl:w-[20%] bg-gray-600 py-2 text-white dark:text-black fixed z-50 right-0"
  >
    <a
      target="_blank"
      href="/"
      class="flex items-center justify-between px-3 py-1"
    >
      <h2 class="text-left">Newtab</h2>
      <p class="text-gray-300">Ctrl+T</p>
    </a>
    <div class="flex justify-between px-3 py-1">
      <h2 class="text-left">New Window</h2>
      <p class="text-gray-300">Ctrl+N</p>
    </div>
    <div class="flex justify-between px-3 py-1">
      <h2 class="text-left">New private Window</h2>
      <p class="text-gray-300">Ctrl+Shift+p</p>
    </div>
    <br />
    <div class="px-3 py-1 text-left">
      <h2 class="text-left">History</h2>
    </div>
    <div class="flex justify-between px-3 py-1">
      <h2 class="text-left">Downloads</h2>
      <p class="text-gray-300">Ctrl+Shift+Y</p>
    </div>
    <div class="px-3 py-1 text-left">
      <h2 class="text-left">Passwords</h2>
    </div>
    <div class="px-3 py-1 text-left">
      <h2 class="text-left">bookmarks</h2>
    </div>
    <br />
    <div class="px-3 py-1 text-left">
      <h2>settings</h2>
    </div>
    <div class="px-3 py-1 text-left">
      <h2 class="text-left">Help</h2>
    </div>
    <div class="px-3 py-1 text-left">
      <h2 class="text-left">More tools</h2>
    </div>
    <br />
  </div>
</template>

<script>
export default {
  name: "TopBar",
  data() {
    return {
      isMenuOpen: false,
    };
  },
  created() {
    document.addEventListener("click", this.dropdown);
  },
  unmounted() {
    document.removeEventListener("click", this.dropdown);
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    dropdown(e) {
      let el = this.$refs.dropdown;
      let target = e.target;
      if (el !== target && !el.contains(target)) {
        this.isMenuOpen = false;
      }
    },
  },
};
</script>

<style>
</style>