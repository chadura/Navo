<template>
  <h1 class="text-gray-200 text-left text-2xl px-5 font-bold dark:text-white">
    General Settings
  </h1>
  <div class="text-left pl-10 dark:bg-gray-700 dark:text-white">
    <section class="flex flex-col gap-y-8 mt-10">
      <div>
        <p class="text-gray-200">More from Navo</p>
        <p class="text-gray-200">
          Checkout other Navo products that work to support healthy internet
        </p>
      </div>

      <div class="flex flex-col gap-y-8">
        <div class="flex">
          <span class="material-symbols-outlined text-gray-200"
            >smartphone</span
          >
          <div class="flex flex-col">
            <h1 class="text-gray-200">Navo Mobile</h1>
            <p class="text-gray-200">
              The Mobile Browser that puts your privacy first
              <span class="text-gray-200 underline">Learn More..</span>
            </p>

            <div
              class="border flex flex-col p-8 w-96 justify-center items-center"
            >
              <p class="flex text-gray-200">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fugiat
                fuga eius omnis vero et corporis sed sit, consectetur magni
                maiores.
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
          <span class="material-symbols-outlined text-gray-200"> token </span>
          <div class="flex flex-col gap-2 text-gray-200">
            <h1 class="text-gray-200">Navo Mobile</h1>
            <p class="text-gray-200">
              The Mobile Browser that puts your privacy first
              <span class="text-blue-400 underline">Learn More..</span>
            </p>
            <button
              class="bg-blue-400 px-2 mt-2 py-2 rounded-lg text-white font-bold"
            >
              Get Relay
            </button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "GeneralSettings",
};
</script>
