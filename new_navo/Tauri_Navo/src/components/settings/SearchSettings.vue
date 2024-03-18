<template>
  <div class="p-5 text-left">
    <div class="flex flex-col gap-2">
      <h1 class="text-gray-200 text-xl font-bold">Search</h1>
      <br />
      <h1 class="text-gray-200 my-2">Default Search Engine</h1>
      <p class="text-gray-200">
        This is your default search engine in the address bar and search bar.
        You can switch it at any time.
      </p>
      <div>
        <select name="" id="" class="border-2 outline-none">
          <option value="">Navo</option>
          <option value="">Navo</option>
          <option value="">Navo</option>
          <option value="">Navo</option>
        </select>
      </div>
    </div>

    <div class="py-8">
      <div class="flex flex-col gap-2">
        <h1 class="text-gray-200">Search Suggestions</h1>
        <p class="text-gray-200">
          Choose how suggestions from search engines appear.
        </p>
        <div class="flex gap-2">
          <input type="checkbox" />
          <p class="text-gray-200">Show search suggestions</p>
        </div>
        <div class="px-5 flex flex-col gap-2">
          <div class="flex gap-2">
            <input type="checkbox" />
            <p class="text-gray-200">
              Show search suggestions ahead of browsing history in address bar
              results
            </p>
          </div>
          <div class="flex gap-2">
            <input type="checkbox" />
            <p class="text-gray-200">
              Show search suggestions in Private Windows
            </p>
          </div>
        </div>
        <a href="" class="underline text-gray-200"
          >Change settings for other address bar suggestions</a
        >
      </div>
    </div>
    <div class="flex flex-col gap-2">
      <h1 class="text-gray-200 text-xl font-bold">Search Shortcuts</h1>
      <p class="text-gray-200 pt-2">
        Choose the alternative search engines that appear below the address bar
        and search bar when you start to enter a keyword.
      </p>
    </div>
    <div class="py-2 my-2">
      <table class="border-2 w-[30%]">
        <thead>
          <tr class="border-2">
            <th class="text-start px-2 py-2 text-gray-200">|SearchEngine</th>
            <th class="text-start px-2 py-2 text-gray-200">|keyword</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-2">
            <td class="px-2 py-2 text-gray-200">Google</td>
            <td class="text-gray-200">@google</td>
          </tr>
          <tr class="border-2">
            <td class="px-2 py-2 text-gray-200">Bing</td>
            <td class="text-gray-200">@bing</td>
          </tr>
          <tr class="border-2">
            <td class="px-2 py-2 text-gray-200">DuckDuckGo</td>
            <td class="text-gray-200">@duckduckgo,@ddg</td>
          </tr>
          <tr class="border-2">
            <td class="px-2 py-2 text-gray-200">Wikipedia(en)</td>
            <td class="text-gray-200">@wikipedia</td>
          </tr>
          <tr class="border-2">
            <td class="px-2 py-2 text-gray-200">Bookmarks</td>
            <td class="text-gray-200">*</td>
          </tr>
          <tr class="border-2">
            <td class="px-2 py-2 text-gray-200">Bing</td>
            <td class="text-gray-200">@bing</td>
          </tr>
          <tr class="border-2">
            <td class="px-2 py-2 text-gray-200">Tabs</td>
            <td class="text-gray-200">%</td>
          </tr>
          <tr class="border-2">
            <td class="px-2 py-2 text-gray-200">History</td>
            <td class="text-gray-200">^</td>
          </tr>
          <tr class="border-2">
            <td class="px-2 py-2 text-gray-200">Action</td>
            <td class="text-gray-200">></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="flex gap-28 py-10">
      <button class="bg-blue-600 text-white py-2 font-bold px-2">
        Restore Default Search Engines
      </button>

      <button class="bg-blue-600 font-bold px-2 text-gray-200">Remove</button>
    </div>
    <div class="py-3">
      <a href="" class="underline text-blue-300">Find more search Engine</a>
    </div>
  </div>
</template>
  
  <script>
export default {
  name: "SearchSettings",
};
</script>
  