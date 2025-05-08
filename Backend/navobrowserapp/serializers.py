from rest_framework import serializers

class SearchResultSerializer(serializers.Serializer):
    title = serializers.CharField()
    href = serializers.CharField()
    body = serializers.CharField()

# class VideoSearchResultSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     href = serializers.CharField(required=False, allow_null=True)
#     body = serializers.CharField(required=False, allow_null=True)