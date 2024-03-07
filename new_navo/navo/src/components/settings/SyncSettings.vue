<template>
  <h1 class="text-gray-500 text-left text-2xl px-5 dark:text-white font-bold">
    Browser Privacy
  </h1>
  <section class="p-10 text-left h-screen flex flex-col gap-y-6">
    <div class="flex justify-between w-3/4">
      <span>
        <h1 class="font-bold">Take Your Web With You</h1>
        <p>
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
    <button class="border px-2 w-2/12">Sign in to Sync..</button>
    <p class="flex items-center gap-x-2">
      Download Firefox for
      <span class="material-symbols-outlined"> android </span> or
      <span class="material-symbols-outlined"> ios </span> to sync with your
      mobile device.
    </p>
  </section>
</template>

<script>
export default {
  name: "SyncSettings",
};
</script>
