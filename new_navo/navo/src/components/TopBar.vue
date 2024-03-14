<template>
  <div
    class="flex bg-gray-600 p-1 gap-x-10 justify-between dark:bg-white dark:text-gray-700"
  >
    <div class="flex items-center gap-x-3">
      <span class="text-left material-symbols-outlined text-lg text-gray-200">
        arrow_back
      </span>
      <span class="text-left material-symbols-outlined text-lg text-gray-200">
        arrow_forward
      </span>
      <span class="text-left material-symbols-outlined text-gray-200 text-lg">
        refresh
      </span>
    </div>

    <div class="flex bg-white items-center rounded-full relative">
      <!-- <input
        type="text"
        class="rounded-xl text-white fold-bold bg-gray-600 outline-none py-2 w-full lg:w-[500px] px-2"
        placeholder="Search Here"
        name=""
        id=""
      /> -->

      <input
        type="text"
        placeholder="Search"
        class="w-full bg-gray-600 text-gray-200 font-bold rounded-xl outline-none p-1 py-3 px-4"
      />

      <router-link
        to="list-page"
        class="flex items-center absolute right-4 shrink-0"
      >
        <div class="w-full">
          <span
            class="shrink-0 text-left w-full text-gray-200 text-base material-symbols-outlined"
          >
            search
          </span>
        </div>
      </router-link>
    </div>
    <div class="flex items-center gap-x-3">
      <button>
        <span class="text-left material-symbols-outlined text-white text-lg">
          bookmarks
        </span>
      </button>

      <router-link to="/profile-login">
        <span class="text-left material-symbols-outlined text-white text-lg">
          account_circle
        </span>
      </router-link>
      <button>
        <span class="text-left material-symbols-outlined text-white text-lg">
          extension
        </span>
      </button>
      <button @click="toggleMenu">
        <span class="text-left material-symbols-outlined text-white text-lg">
          menu
        </span>
      </button>
    </div>
  </div>
  <div
    v-if="isMenuOpen"
    class="shadow-md lg:w-[35%] xl:w-[20%] bg-gray-600 py-2 text-white fixed z-50 right-0"
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
      <router-link to="/settings">settings</router-link>
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
  components: {},
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
};
</script>
