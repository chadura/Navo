<template>
    <h1 class="text-gray-200 text-left text-2xl px-5 font-bold">
      Browser Privacy
    </h1>
    <section class="p-10 text-left h-screen flex flex-col gap-y-6">
      <div class="flex justify-between w-3/4">
        <span>
          <h1 class="font-bold text-gray-200">Take Your Web With You</h1>
          <p class="text-gray-200">
            Synchronize your bookmarks, history, tabs, passwords, add-ons, and
            settings across all your devices.
          </p></span
        >
        <img
          src="https://assets-prod.sumo.prod.webservices.mozgcp.net/media/uploads/gallery/images/2019-11-27-13-05-18-63ad9d.png"
          alt=""
          class="object-contain"
        />
      </div>
      <button class="border px-2 w-2/12 text-gray-200 py-2">
        Sign in to Sync..
      </button>
      <p class="flex items-center gap-x-2 text-gray-200">
        Download Firefox for
        <span class="material-symbols-outlined text-gray-200"> android </span> or
        <span class="material-symbols-outlined text-gray-200"> ios </span> to sync
        with your mobile device.
      </p>
    </section>
  </template>
  
  <script>
  export default {
    name: "SyncSettings",
  };
  </script>
  