<template class="">
  <div class="max-h-screen overflow-hidden">
    <TopBar />
    <div
      class="flex justify-center items-center rounded-xl h-screen overflow-hidden"
    >
      <div class="shadow-md w-[35%] rounded-lg border h-auto p-3">
        <div>
          <h2 class="text-center py-5 text-xl font-bold">
            Continue to your Navo account
          </h2>
          <p class="text-center text-sm">
            Sync your Passwords,tabs,and bookmarks everywhere you use firefox.
          </p>
        </div>
        <div class="py-5 text-center">
          <input
            type="email"
            class="border-2 w-[70%] h-[50px] px-5 rounded-md"
            placeholder="  Enter your email"
          />
        </div>
        <div class="text-center">
          <button
            class="bg-blue-600 text-white font-bold w-[70%] h-[50px] rounded-md"
          >
            Sign up or sign in
          </button>
        </div>
        <div class="py-5 text-sm text-gray-600">
          <p class="text-center">
            A Navo account also unlock access to more privacy-protecting
          </p>
          <p class="text-center">products from Navo</p>
        </div>
        <div class="py-1 text-sm text-center text-gray-600">
          <p>
            By proceeding,you agree to the
            <a href="" class="underline">Terms of Service</a> and
            <a href="" class="underline">Privacy Notice</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
import TopBar from "./components/TopBar.vue";
export default {
  name: "ProfileLogin",
  components: {
    TopBar,
  },
};