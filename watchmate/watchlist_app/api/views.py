from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatForm, Reviews
from django.http import JsonResponse
from watchlist_app.api.serializers import WatchListSerializers, StreamPlatFormSerializers, ReviewsSerializers 
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from rest_framework import status

from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins

class ReviewList(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers 

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
    
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializers

#     def get(self, request,  *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetails(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
    
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializers 
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
        
class StreamPlatFormAV(APIView):
    def get(self, request):
        streamPlatForm = StreamPlatForm.objects.all()
        serializer = StreamPlatFormSerializers(streamPlatForm, many = True, context={'request': request})
        return Response(serializer.data)


    def post(self, request):
        serializer = StreamPlatFormSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatFormDetailAV(APIView):
    def get(self, request, pk):
        try:
            streamPlatForm = StreamPlatForm.objects.get(pk=pk)
        except StreamPlatForm.DoesNotExists:
            return Response({'error: Movie not found'}, status = status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatFormSerializers(streamPlatForm) 
        return Response(serializer.data)


    def put(self, request, pk):
        streamplt = StreamPlatForm.objects.get(pk=pk)
        serializer = StreamPlatFormSerializers(streamplt,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # return Response(serializer.errors)
            return Response(serializers.error, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        streamplt = StreamPlatForm.objects.get(pk=pk)
        streamplt.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializers(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchListDetailAV(APIView):
    def get(self, request, pk):
        
        try:
            movie = WatchList.objects.get(pk=pk)
        except Movie.DoesNotExists:
            return Response({'errors: Movie not found'}, status = status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializers(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializers(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializers.error, status = status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    








 