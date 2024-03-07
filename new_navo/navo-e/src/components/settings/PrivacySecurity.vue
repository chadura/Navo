<template>
  <h1 class="text-gray-500 text-left px-10 text-2xl dark:text-white font-bold">
    Browser Privacy
  </h1>
  <section class="text-left flex flex-col px-16 gap-y-6">
    <h1 class="font-bold">Enhanced Tracking Protection</h1>
    <div class="flex gap-x-5 w-full tems-center">
      <span class="material-symbols-outlined text-4xl"> shield </span>
      <p class="flex flex-wrap">
        Trackers follow you around online to collect information about your
        browsing habits and interests. Firefox blocks many of these trackers and
        other malicious scripts.
      </p>
      <button class="p-2 border rounded-lg">Manage Exceptions...</button>
    </div>

    <!-- Accordian -->
    <div
      class="bg-[#16424E] flex flex-col gap-y-2 w-1/2 p-5 focus:bg-blue-700 text-white text-left"
    >
      <div class="flex">
        <input type="radio" name="" id="" /> <label for="">Standard</label>
      </div>
      <p class="font-bold">
        Balanced for protection and performance. Pages will load normally.
      </p>
      <p class="font-bold">Firefox blocks the following:</p>
      <ul class="list lis">
        <li>&nbsp; Social media trackers</li>
        <li>&nbsp; Cross-site cookies in all windows</li>
        <li>&nbsp; Tracking content in Private Windows</li>
        <li>&nbsp; Cryptominers</li>
        <li>&nbsp; Fingerprinters</li>
      </ul>
      <div class="border p-5 bg-[#126171]">
        <p>
          <span class="font-bold"
            >Includes Total Cookie Protection, our most powerful privacy feature
            ever</span
          >
          Total Cookie Protection contains cookies to the site you’re on, so
          trackers can’t use them to follow you between sites.
        </p>
      </div>
    </div>
    <p class="font-bold">Website Privacy Preferences</p>
    <div class="flex gap-x-2">
      <input type="checkbox" />
      <label for="">Tell websites not to sell or share my data</label>
    </div>
    <div class="flex gap-x-2">
      <input type="checkbox" />
      <label for="">Send websites a “Do Not Track” request</label>
    </div>

    <p class="font-bold">Cookies and Site Data</p>
    <div class="flex items-center">
      <table>
        <tr>
          <td clas>
            Your stored cookies, site data, and cache are currently using 1.0 GB
            of disk space
          </td>
          <td class="w-full">
            <button class="border p-2 px-4">Clear Data</button>
          </td>
        </tr>
        <tr>
          <td class="w-full"></td>
          <td class="w-full">
            <button class="border p-2 px-4">Manage Data</button>
          </td>
        </tr>
        <tr>
          <td class="w-full">
            <input type="checkbox" name="" id="" /> Delete cookies and site data
            when Firefox is closed
          </td>
          <td class="w-full">
            <button class="border p-2 px-4">Manage Exception</button>
          </td>
        </tr>
      </table>
    </div>
    <div class="flex flex-col gap-y-1">
      <h1 class="font-bold">Passwords</h1>
      <div class="flex w-3/4 justify-between">
        <span
          ><input type="checkbox" name="" id="" /><label for=""
            >Ask to save passwords</label
          ></span
        ><button class="border px-4">Exception</button>
      </div>
      <div class="flex w-3/4 justify-between">
        <span
          >&nbsp;<input type="checkbox" name="" id="" /><label for=""
            >Fill usernames and passwords automatically</label
          ></span
        ><button class="border px-4">Save Passwords</button>
      </div>
      <span
        >&nbsp;<input type="checkbox" name="" id="" /><label for=""
          >Suggest strong passwords</label
        ></span
      >
      <span
        >&nbsp;<input type="checkbox" name="" id="" /><label for=""
          >Suggest Firefox Relay email masks to protect your email
          address</label
        ></span
      >
    </div>
  </section>
</template>

<script>
export default {
  name: "PrivacySettings",
};
</script>
