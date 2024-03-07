<template>
  <TopBar />
  <div>
    <SettingsBrowser />
  </div>
</template>

<script>
import SettingsBrowser from "@/components/settings/SettingsBrowser.vue";
import TopBar from "@/components/TopBar.vue";
export default {
  name: "SettingsView",
  components: {
    SettingsBrowser,
    TopBar,
  },
};
</script>

<style></style>
