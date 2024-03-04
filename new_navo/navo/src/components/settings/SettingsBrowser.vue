<template>
  <div class="dark:bg-gray-700 dark:text-white">
    <div class="w-full flex">
      <div
        class="w-[30%] mflex flex-col items-center border-r justify-center p-10 gap-y-5"
      >
        <button
          class="hover:bg-gray-400 w-full"
          @click="setActive('GeneralSettings')"
        >
          <h1 class="flex items-center">
            <span class="material-symbols-outlined"> settings </span
            >&nbsp;General
          </h1>
        </button>
        <button
          class="hover:bg-gray-400 w-full"
          @click="setActive('HomeSettings')"
        >
          <h1 class="flex items-center">
            <span class="material-symbols-outlined"> home </span>&nbsp;Home
          </h1>
        </button>
        <button
          @click="setActive('SearchSettings')"
          class="hover:bg-gray-400 w-full"
        >
          <h1 class="flex items-center">
            <span class="material-symbols-outlined"> search </span>&nbsp;Search
          </h1>
        </button>
        <button
          class="hover:bg-gray-400 w-full"
          @click="setActive('PrivacySecurity')"
        >
          <h1 class="flex items-center">
            <span class="material-symbols-outlined"> lock </span>&nbsp;Privacy &
            Security
          </h1>
        </button>
        <button
          @click="setActive('SyncSettings')"
          class="hover:bg-gray-400 w-full"
        >
          <h1 class="flex items-center">
            <span class="material-symbols-outlined"> sync </span>&nbsp;Sync
          </h1>
        </button>
      </div>
      <div class="w-full">
        <div class="flex items-center justify-center pt-2">
          <input
            type="search"
            class="border"
            placeholder="Find in Settings"
          /><span class="border material-symbols-outlined"> Search </span>
        </div>
        <GeneralSettings v-if="isActive === 'GeneralSettings'" />
        <PrivacySecurity v-if="isActive === 'PrivacySecurity'" />
        <SyncSettings v-if="isActive === 'SyncSettings'" />
        <SearchSettings v-if="isActive === 'SearchSettings'" />
        <HomeSettings v-if="isActive === 'HomeSettings'" />
      </div>
    </div>
  </div>
</template>

<script>
import PrivacySecurity from "./PrivacySecurity.vue";
import GeneralSettings from "./GeneralSettings.vue";
import SyncSettings from "./SyncSettings.vue";
import HomeSettings from "./HomeSettings.vue";
import SearchSettings from "./SearchSettings.vue";

export default {
  name: "SettingsBrowser",
  data() {
    return {
      isActive: "GeneralSettings",
    };
  },
  methods: {
    setActive(componentName) {
      this.isActive = componentName;
    },
  },
  components: {
    GeneralSettings,
    PrivacySecurity,
    SyncSettings,
    SearchSettings,
    HomeSettings,
  },
};
</script>

<style></style>
