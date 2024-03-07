<template>
  <TopBar />
  <div class="w-full text-left mx-auto h-screen bg-gray-800">
    <div
      class="flex items-start p-5 gap-x-10 sticky top-[72px] bg-gray-800 z-40"
    >
      <div class="flex flex-row gap-1">
        <img src="@/assets/navo-icon.png" class="w-[50px] h-[50px]" />
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
                src="data:image/png;base64,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"
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

<script>
import TopBar from "@/components/TopBar.vue";
export default {
  name: "ListView",
  components: {
    TopBar,
  },
};
</script>

<style></style>
