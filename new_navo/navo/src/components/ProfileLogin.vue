<template>
  <div class="flex justify-center items-center h-screen">
    <div class="shadow-md w-[35%] h-[380px] rounded-xl bg-slate-100">
      <div>
        <h2 class="text-center py-5 text-xl font-bold">
          Continue to your Mozilla account
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
          A Mozile account also unlock access to more privacy-protecting
        </p>
        <p class="text-center">products from Mozilla</p>
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
</template>

<script>
export default {
  name: "ProfileLogin",
};
</script>
