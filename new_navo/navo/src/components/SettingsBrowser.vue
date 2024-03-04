<template>
  <div>
    <div class="w-full flex">
      <div
        class="w-[20%] mflex flex-col items-start border-r justify-center p-10 gap-y-5 hidden"
      >
        <button class="hover:bg-gray-400 w-full">
          <h1 class="flex items-center">
            <span class="material-symbols-outlined"> settings </span
            >&nbsp;General
          </h1>
        </button>
        <button class="hover:bg-gray-400 w-full">
          <h1 class="flex items-center">
            <span class="material-symbols-outlined"> home </span>&nbsp;Home
          </h1>
        </button>
        <button class="hover:bg-gray-400 w-full">
          <h1 class="flex items-center">
            <span class="material-symbols-outlined"> search </span>&nbsp;Search
          </h1>
        </button>
        <button class="hover:bg-gray-400 w-full">
          <h1 class="flex items-center">
            <span class="material-symbols-outlined"> lock </span>&nbsp;Privacy &
            Security
          </h1>
        </button>
        <button class="hover:bg-gray-400 w-full">
          <h1 class="flex items-center">
            <span class="material-symbols-outlined"> sync </span>&nbsp;Sync
          </h1>
        </button>
      </div>
      <div
        class="w-[20%] flex flex-col items-start border-r justify-center p-10 gap-y-5"
      >
        <div v-for="setting in settingsData" :key="setting.id">
          <button class="hover:bg-gray-400 w-full">
            <h1 class="flex items-center">
              <span class="material-symbols-outlined"> {{ setting.icon }} </span
              >&nbsp;{{ setting.title }}
            </h1>
          </button>
        </div>
      </div>
      <div class="w-[80%] pl-10">
        <div class="flex items-center justify-center">
          <input
            type="search"
            class="border"
            placeholder="Find in Settings"
          /><span class="border material-symbols-outlined"> Search </span>
        </div>

        <section class="flex flex-col gap-y-8 mt-10">
          <div>
            <p>More from Nova</p>
            <p>
              Checkout other Nova products that work to support healthy internet
            </p>
          </div>

          <div class="flex flex-col gap-y-8">
            <div class="flex">
              <span class="material-symbols-outlined">smartphone</span>
              <div class="flex flex-col">
                <h1>Nova Mobile</h1>
                <p>
                  The Mobile Browser that puts your privacy first
                  <span class="text-blue-400 underline">Learn More..</span>
                </p>

                <div
                  class="border flex flex-col p-8 w-96 justify-center items-center"
                >
                  <p class="flex">
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                    Fugiat fuga eius omnis vero et corporis sed sit, consectetur
                    magni maiores.
                  </p>
                  <img
                    src="https://cdn.britannica.com/17/155017-050-9AC96FC8/Example-QR-code.jpg"
                    class="h-20"
                    alt=""
                  />
                </div>
              </div>
            </div>
            <div class="flex">
              <span class="material-symbols-outlined"> token </span>
              <div class="flex flex-col">
                <h1>Nova Mobile</h1>
                <p>
                  The Mobile Browser that puts your privacy first
                  <span class="text-blue-400 underline">Learn More..</span>
                </p>
                <button
                  class="bg-blue-400 rounded-lg w-20 mt-5 text-white font-bold"
                >
                  Get Relay
                </button>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SettingsBrowser",
  data() {
    return {
      settingsData: [
        {
          id: 1,
          icon: "settings",
          title: "General",
        },
        {
          id: 2,
          icon: "home",
          title: "Home",
        },
        {
          id: 3,
          icon: "search",
          title: "Search",
        },
        {
          id: 4,
          icon: "lock",
          title: "Privacy & Security",
        },
        {
          id: 5,
          icon: "sync",
          title: "Sync",
        },
      ],
    };
  },
};
</script>

<style></style>
