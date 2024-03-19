<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import TopBar from "./components/TopBar.vue";
</script>

<template>
  <TopBar />
  <div class="w-full text-left mx-auto h-screen bg-gray-800">
    <div
      class="flex items-start p-5 gap-x-10 sticky top-[72px] bg-gray-800 z-40"
    >
      <div class="flex flex-row gap-1">
        <img src="./assets/navo-icon.png" class="w-[50px] h-[50px]" />
        <a
          href="https://www.google.com"
          class="py-2 text-2xl font-semibold text-gray-200"
          >Navo</a
        >
      </div>

      <div class="w-full flex flex-col gap-y-6">
        <input
          type="search"
          placeholder="search"
          class="w-full lg:w-[60%] bg-gray-600 text-gray-200 font-bold rounded-xl outline-none p-1 py-3 px-4"
        />
        <div class="flex flex-wrap gap-y-2 gap-x-2 justify-start">
          <button
            class="text-sm text-gray-200 py-1 rounded-full px-3 hover:bg-gray-400"
          >
            Images
          </button>
          <button
            class="text-sm text-gray-200 py-1 rounded-full px-3 hover:bg-gray-400"
          >
            Videos
          </button>
          <button
            class="text-sm text-gray-200 py-1 rounded-full px-3 hover:bg-gray-400"
          >
            Download
          </button>
          <button
            class="text-sm text-gray-200 py-1 rounded-full px-3 hover:bg-gray-400"
          >
            Compiler
          </button>
          <button
            class="text-sm text-gray-200 py-1 rounded-full px-3 hover:bg-gray-400"
          >
            Code
          </button>
          <button
            class="text-sm text-gray-200 py-1 rounded-full px-3 hover:bg-gray-400"
          >
            Learn
          </button>
          <button
            class="text-sm text-gray-200 py-1 rounded-full px-3 hover:bg-gray-400"
          >
            Shopping
          </button>
          <button
            class="text-sm text-gray-200 py-1 rounded-full px-3 hover:bg-gray-400"
          >
            Online
          </button>
          <button
            class="text-sm text-gray-200 py-1 rounded-full px-3 hover:bg-gray-400"
          >
            W3schools
          </button>
        </div>
      </div>
      <img
        src="https://images.unsplash.com/photo-1633332755192-727a05c4013d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dXNlcnxlbnwwfHwwfHx8MA%3D%3D"
        class="shadow-lg rounded-full h-10 w-10 object-contain"
        alt=""
      />
    </div>

    <div class="bg-gray-800">
      <div class="container mx-auto max-w-[1700px] px-6">
        <div
          class="w-full flex py-10 flex-col gap-y-6 items-start justify-center"
        >
          <div v-for="i in 10" :key="i" class="flex flex-col gap-y-2">
            <div class="flex gap-x-3">
              <img
                src="../src/assets/navo-icon.png"
                class="h-5 w-5 my-2 rounded-full"
                alt=""
              />
              <div class="flex flex-col">
                <p class="text-sm font-bold text-gray-200">Python</p>
                <a href="https://www.python.org" class="text-xs text-gray-200"
                  >www.Python.org</a
                >
              </div>
            </div>
            <div class="text-left flex flex-col gap-3 w-full lg:w-[60%]">
              <a href="#" class="text-lg text-gray-200 font-semibold"
                >Python Openings</a
              >
              <p class="flex-wrap text-sm text-gray-200">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Nostrum, maiores quisquam nemo autem deserunt nisi magnam. Iste
                distinctio tempora deserunt. Tenetur reprehenderit amet
                inventore adipisci quo soluta! Ratione, nihil tempora.
              </p>
            </div>
          </div>
        </div>

        <div class="flex justify-center gap-x-2 bottom-0">
          <a href="" class="text-gray-200">1</a>
          <a href="" class="text-gray-200">2</a>
          <a href="" class="text-gray-200">3</a>
          <a href="" class="text-gray-200">4</a>
          <a href="" class="text-gray-200">Next</a>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
</style>

