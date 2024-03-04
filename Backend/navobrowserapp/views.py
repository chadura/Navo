from django.shortcuts import render
from django.http import HttpResponse
import asyncio
from .async_ddgs import AsyncDDGS
from django.http import JsonResponse


# REFERENCE : https://github.com/deedy5/duckduckgo_search

# Example: Search for "python programming" and get the first 5 results

# from duckduckgo_search import DDGS

# results = DDGS().text("python programming", max_results=5)
# print(results)

# You can use DDGS also as context manager
# with DDGS() as ddgs:
#     results = ddgs.text("python programming", max_results=5)
#     print(results)

async def search_ddg(keywords):
    async with AsyncDDGS() as ddgs:
        # keywords = "python programming" # The keywords to search for
        # max_results = 5 # The maximum number of results to return (avoid blocking from api by reducing the number of results)
        results = await ddgs.text(keywords, max_results=15)
    return results

def index(request):
    if request.method == "GET":
        return render(request, "search_app/index.html")
    elif request.method == "POST":
        keywords = request.POST.get("keywords", "")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(search_ddg(keywords))
        return render(request, "search_app/index.html", {"results": results})

async def autocomplete(request):
    query = request.GET.get('query', '')

    # Call the search_ddg function to get autocomplete suggestions asynchronously
    results = await search_ddg(query)

    # Extract titles from the search results to use as autocomplete suggestions
    suggestions = [{'title': result['title'], 'href': result['href']} for result in results]

    # Return the autocomplete suggestions as JSON response
    return JsonResponse({'results': suggestions})