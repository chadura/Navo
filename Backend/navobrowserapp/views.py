from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.response import Response
import asyncio
from .async_ddgs import AsyncDDGS
from .serializers import SearchResultSerializer 
from rest_framework import status

class SearchDDGView(generics.GenericAPIView):
    serializer_class = SearchResultSerializer

    async def search_ddg(self, keywords):
        async with AsyncDDGS() as ddgs:
            results = await ddgs.text(keywords, max_results=100)
        return results

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query', '')
        
        if not query:
            try:
                data = request.data
                query = data.get('query', '')
            except Exception as e:
                return Response({'error': 'Error parsing JSON input'}, status=status.HTTP_400_BAD_REQUEST)

        if not query:
            return Response({'error': 'Query parameter is missing or empty'}, status=status.HTTP_400_BAD_REQUEST)

        results = asyncio.run(self.search_ddg(query))

        serializer = self.get_serializer(results, many=True)
        return Response({'results': serializer.data})


class IndexView(TemplateView):
    template_name = "search_app/index.html"


class AutocompleteView(generics.GenericAPIView):
    serializer_class = SearchResultSerializer

    async def search_ddg(self, keywords):
        async with AsyncDDGS() as ddgs:
            results = await ddgs.text(keywords, max_results=100)
        return results

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query', '')
        results = asyncio.run(self.search_ddg(query))

        serializer = self.get_serializer(results, many=True)
        return Response({'results': serializer.data})


# class VideoSearchView(generics.GenericAPIView):
#     serializer_class = VideoSearchResultSerializer

#     async def search_videos(self, keywords, max_results=100):
#         async with AsyncDDGS() as ddgs:
#             video_results = await ddgs.videos(keywords, max_results=max_results)
#         return video_results

#     def get(self, request, *args, **kwargs):
#         query = self.request.GET.get('query', '')
        
#         if not query:
#             try:
#                 data = request.data
#                 query = data.get('query', '')
#                 print('query', query)
#             except Exception as e:
#                 return Response({'error': 'Error parsing JSON input'}, status=status.HTTP_400_BAD_REQUEST)
#             if not query:
#                 return Response({'error': 'Query parameter is missing or empty'}, status=status.HTTP_400_BAD_REQUEST)

#             video_results = asyncio.run(self.search_videos(query))

#             # Filter out results without 'href' field
#             valid_results = [result for result in video_results if 'href' in result]

#             serializer = self.get_serializer(video_results, many=True)
#             return Response({'video_results': serializer.data})