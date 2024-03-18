<template>
  <h1 class="text-gray-200 text-left px-10 text-2xl font-bold">
    Browser Privacy
  </h1>
  <section class="text-left flex flex-col px-16 gap-y-6 mt-6 bg-gray-800">
    <h1 class="font-bold text-gray-200">Enhanced Tracking Protection</h1>
    <div class="flex gap-x-5 w-full tems-center">
      <span class="material-symbols-outlined text-4xl text-gray-200">
        shield
      </span>
      <p class="flex flex-wrap text-gray-200">
        Trackers follow you around online to collect information about your
        browsing habits and interests. Firefox blocks many of these trackers and
        other malicious scripts.
      </p>
      <button class="p-2 border rounded-lg text-gray-200">
        Manage Exceptions...
      </button>
    </div>

    <!-- Accordian -->
    <div
      class="bg-[#16424E] flex flex-col gap-y-2 w-1/2 p-5 focus:bg-blue-700 text-white text-left"
    >
      <div class="flex gap-2">
        <input type="radio" name="" id="" />
        <label for="" class="text-gray-200">Standard</label>
      </div>
      <p class="font-bold text-gray-200">
        Balanced for protection and performance. Pages will load normally.
      </p>
      <p class="font-bold text-gray-200">Firefox blocks the following:</p>
      <ul class="list lis">
        <li class="text-gray-200">&nbsp; Social media trackers</li>
        <li class="text-gray-200">&nbsp; Cross-site cookies in all windows</li>
        <li class="text-gray-200">
          &nbsp; Tracking content in Private Windows
        </li>
        <li class="text-gray-200">&nbsp; Cryptominers</li>
        <li class="text-gray-200">&nbsp; Fingerprinters</li>
      </ul>
      <div class="border p-5 bg-[#126171]">
        <p class="text-gray-200">
          <span class="font-bold text-gray-200"
            >Includes Total Cookie Protection, our most powerful privacy feature
            ever</span
          >
          Total Cookie Protection contains cookies to the site you’re on, so
          trackers can’t use them to follow you between sites.
        </p>
      </div>
    </div>
    <p class="font-bold text-gray-200">Website Privacy Preferences</p>

    <div class="flex flex-col gap-1">
      <div class="flex gap-x-2">
        <input type="checkbox" />
        <label class="text-gray-200" for=""
          >Tell websites not to sell or share my data</label
        >
      </div>
      <div class="flex gap-x-2">
        <input type="checkbox" />
        <label class="text-gray-200" for=""
          >Send websites a “Do Not Track” request</label
        >
      </div>
    </div>

    <p class="font-bold text-gray-200">Cookies and Site Data</p>
    <div class="flex items-center">
      <table>
        <tr>
          <td class="text-gray-200">
            Your stored cookies, site data, and cache are currently using 1.0 GB
            of disk space
          </td>
          <td class="w-full">
            <button class="border p-2 px-4 text-gray-200">Clear Data</button>
          </td>
        </tr>
        <tr>
          <td class="w-full"></td>
          <td class="w-full">
            <button class="border p-2 px-4 text-gray-200">Manage Data</button>
          </td>
        </tr>
        <tr>
          <td class="w-full text-gray-200">
            <input type="checkbox" name="" id="" /> Delete cookies and site data
            when Firefox is closed
          </td>
          <td class="w-full">
            <button class="border p-2 px-4 text-gray-200">
              Manage Exception
            </button>
          </td>
        </tr>
      </table>
    </div>
    <div class="flex flex-col gap-y-2">
      <h1 class="font-bold text-gray-200">Passwords</h1>

      <div class="flex gap-2">
        <span class="flex gap-2"
          ><input type="checkbox" name="" id="" /><label
            for=""
            class="text-gray-200"
            >Ask to save passwords</label
          ></span
        ><button class="border px-4 text-gray-200">Exception</button>
      </div>
      <div class="flex gap-2">
        <span class="flex gap-2"
          >&nbsp;<input type="checkbox" name="" id="" /><label
            for=""
            class="text-gray-200"
            >Fill usernames and passwords automatically</label
          ></span
        ><button class="border px-4 text-gray-200">Save Passwords</button>
      </div>
      <span class="flex gap-2"
        >&nbsp;<input type="checkbox" name="" id="" /><label
          for=""
          class="text-gray-200"
          >Suggest strong passwords</label
        ></span
      >
      <span class="flex gap-2"
        >&nbsp;<input type="checkbox" name="" id="" /><label
          for=""
          class="text-gray-200"
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
  