<template>
  <div
    class="flex bg-gray-600 p-1 py-4 gap-x-10 justify-between dark:bg-white dark:text-gray-700"
  >
    <div class="flex gap-x-3">
      <span
        class="material-symbols-outlined text-lg text-white dark:text-black"
      >
        arrow_back
      </span>
      <span
        class="material-symbols-outlined text-lg text-white dark:text-black"
      >
        arrow_forward
      </span>
      <span
        class="material-symbols-outlined text-white dark:text-black text-lg"
      >
        refresh
      </span>
    </div>
    <div class="flex bg-white items-center rounded-full relative">
      <input
        type="text"
        class="rounded-full border border-solid outline-none py-2 w-full px-2"
        placeholder="Search Here"
        name=""
        id=""
      />
      <router-link to="list-page" class="flex items-center absolute right-0">
        <span class="material-symbols-outlined"> search </span>
      </router-link>
    </div>
    <div class="flex items-center gap-x-3">
      <button>
        <span
          class="material-symbols-outlined text-white dark:text-black text-lg"
        >
          bookmarks
        </span>
      </button>

      <router-link to="/profile-login">
        <span
          class="material-symbols-outlined text-white dark:text-black text-lg"
        >
          account_circle
        </span>
      </router-link>
      <button>
        <span
          class="material-symbols-outlined text-white dark:text-black text-lg"
        >
          extension
        </span>
      </button>
      <button @click="toggleMenu">
        <span
          class="material-symbols-outlined text-white dark:text-black text-lg"
        >
          menu
        </span>
      </button>
    </div>
  </div>
  <div
    v-if="isMenuOpen"
    class="shadow-md w-[20%] bg-gray-500 text-white dark:text-white absolute z-10 right-0"
  >
    <a target="_blank" href="/" class="flex items-center justify-between px-3">
      <h2>Newtab</h2>
      <p class="text-gray-300">Ctrl+T</p>
    </a>
    <div class="flex justify-between px-3">
      <h2>New Window</h2>
      <p class="text-gray-300">Ctrl+N</p>
    </div>
    <div class="flex justify-between px-3">
      <h2>New private Window</h2>
      <p class="text-gray-300">Ctrl+Shift+p</p>
    </div>
    <br />
    <div class="px-3 text-left">
      <h2>History</h2>
    </div>
    <div class="flex justify-between px-3">
      <h2>Downloads</h2>
      <p class="text-gray-300">Ctrl+Shift+Y</p>
    </div>
    <div class="px-3 text-left">
      <h2>Passwords</h2>
    </div>
    <div class="px-3 text-left">
      <h2>bookmarks</h2>
    </div>
    <br />
    <div class="px-3 text-left">
      <router-link to="/settings">settings</router-link>
    </div>
    <div class="px-3 text-left">
      <h2>Help</h2>
    </div>
    <div class="px-3 text-left">
      <h2>More tools</h2>
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
  components: {},
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
};
</script>
