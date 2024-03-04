<template>
  <div class="p-5 text-left">
    <div>
      <h1 class="text-gray-500 text-xl">Search</h1>
      <br />
      <h1>Default Search Engine</h1>
      <p class="text-gray-500">
        This is your default search engine in the address bar and search bar.
        You can switch it at any time.
      </p>
      <select name="" id="" class="border-2">
        <option value="">Google</option>
        <option value="">Bing</option>
        <option value="">Google</option>
        <option value="">Google</option>
      </select>
    </div>

    <div class="py-8">
      <div>
        <h1>Search Suggestions</h1>
        <p class="text-gray-500">
          Choose how suggestions from search engines appear.
        </p>
        <div class="flex">
          <input type="checkbox" />
          <p>Show search suggestions</p>
        </div>
        <div class="px-5">
          <div class="flex">
            <input type="checkbox" />
            <p>
              Show search suggestions ahead of browsing history in address bar
              results
            </p>
          </div>
          <div class="flex">
            <input type="checkbox" />
            <p>Show search suggestions in Private Windows</p>
          </div>
        </div>
        <a href="" class="text-blue-400 underline"
          >Change settings for other address bar suggestions</a
        >
      </div>
    </div>
    <div>
      <h1>Search Shortcuts</h1>
      <p class="text-gray-500">
        Choose the alternative search engines that appear below the address bar
        and search bar when you start to enter a keyword.
      </p>
    </div>
    <div class="py-2">
      <table class="border-2 w-[30%]">
        <thead>
          <tr class="border-2 bg-gray-300">
            <th class="text-start px-2">|SearchEngine</th>
            <th class="text-start px-2">|keyword</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-2">
            <td class="px-2">Google</td>
            <td>@google</td>
          </tr>
          <tr class="border-2 bg-gray-300">
            <td class="px-2">Bing</td>
            <td>@bing</td>
          </tr>
          <tr class="border-2">
            <td class="px-2">DuckDuckGo</td>
            <td>@duckduckgo,@ddg</td>
          </tr>
          <tr class="border-2 bg-gray-300">
            <td class="px-2">Wikipedia(en)</td>
            <td>@wikipedia</td>
          </tr>
          <tr class="border-2">
            <td class="px-2">Bookmarks</td>
            <td>*</td>
          </tr>
          <tr class="border-2 bg-gray-300">
            <td class="px-2">Bing</td>
            <td>@bing</td>
          </tr>
          <tr class="border-2">
            <td class="px-2">Tabs</td>
            <td>%</td>
          </tr>
          <tr class="border-2 bg-gray-300">
            <td class="px-2">History</td>
            <td>^</td>
          </tr>
          <tr class="border-2">
            <td class="px-2">Action</td>
            <td>></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="flex gap-28">
      <button class="border-2 bg-gray-300 font-bold px-2">
        Restore Default Search Engines
      </button>

      <button class="border-2 bg-slate-300 font-bold px-2">Remove</button>
    </div>
    <div class="py-3">
      <a href="" class="text-blue-400 underline">Find more search Engine</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchSettings",
};
</script>
