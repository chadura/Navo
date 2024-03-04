<template>
  <h1 class="text-gray-500 text-left text-2xl px-5 font-bold dark:text-white">
    General Settings
  </h1>
  <div class="text-left pl-10 dark:bg-gray-700 dark:text-white">
    <section class="flex flex-col gap-y-8 mt-10">
      <div>
        <p>More from Navo</p>
        <p>
          Checkout other Navo products that work to support healthy internet
        </p>
      </div>

      <div class="flex flex-col gap-y-8">
        <div class="flex">
          <span class="material-symbols-outlined">smartphone</span>
          <div class="flex flex-col">
            <h1>Navo Mobile</h1>
            <p>
              The Mobile Browser that puts your privacy first
              <span class="text-blue-400 underline">Learn More..</span>
            </p>

            <div
              class="border flex flex-col p-8 w-96 justify-center items-center"
            >
              <p class="flex">
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
          <span class="material-symbols-outlined"> token </span>
          <div class="flex flex-col">
            <h1>Navo Mobile</h1>
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
</template>

<script>
export default {
  name: "GeneralSettings",
};
</script>
