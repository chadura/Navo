<template>
  <div class="relative bg-blue-400">
    <div class="flex bg-gray-600 p-1 gap-x-10 justify-between">
      <div class="flex gap-x-3">
        <span class="material-symbols-outlined text-lg text-white">
          arrow_back
        </span>
        <span class="material-symbols-outlined text-lg text-white">
          arrow_forward
        </span>
        <span class="material-symbols-outlined text-white text-lg">
          refresh
        </span>
      </div>
      <div class="flex bg-white rounded-full">
        <input
          type="search"
          v-model="search.query"
          class="rounded-full w-full px-2"
          placeholder="Search Here"
          name=""
          id=""
        />
        <router-link to="list" class="flex items-center">
          <span class="material-symbols-outlined"> search </span>
        </router-link>
      </div>
      <div class="flex gap-x-3">
        <button>
          <span class="material-symbols-outlined text-white text-lg">
            bookmarks
          </span>
        </button>

        <button>
          <span class="material-symbols-outlined text-white text-lg">
            account_circle
          </span>
        </button>
        <button>
          <span class="material-symbols-outlined text-white text-lg">
            extension
          </span>
        </button>
        <button @click="toggleMenu">
          <span class="material-symbols-outlined text-white text-lg">
            menu
          </span>
        </button>
      </div>
    </div>
    <div
      v-if="isMenuOpen"
      class="shadow-md w-[20%] bg-gray-500 text-white absolute right-0"
    >
      <div class="flex justify-between px-3">
        <h2>Newtab</h2>
        <p class="text-gray-300">Ctrl+T</p>
      </div>
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
        <!-- <a href="" target="_blank">Settings</a> -->
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
    <div class="flex flex-col items-center h-screen justify-center gap-y-5">
      <h1 class="text-2xl font-sans">NAVO</h1>
      <div class="flex bg-white w-[50%] rounded-full">
        <input
          type="search"
          v-model="search.query"
          class="w-[90%] border rounded-full p-1 focus:"
          placeholder="What you are looking for?"
          name=""
          id=""
        />
        <button class="flex items-center">
          <span class="material-symbols-outlined"> search </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      isMenuOpen: false,
      search: {
        query: "",
      },
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
