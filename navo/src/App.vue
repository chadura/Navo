<script setup>
import Greet from "./components/Greet.vue";
</script>

<template>
  <div class="container bg-green-200">
    <form class="row" @submit.prevent="greet">
      <input class="bg-red-300" id="greet-input" v-model="name" placeholder="Enter address..." />
    <button type="submit">Greet</button>
  </form>
    
  </div>
</template>

<style>

</style>