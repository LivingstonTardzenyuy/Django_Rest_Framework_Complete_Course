from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatForm, Reviews
from django.http import JsonResponse
from watchlist_app.api.serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from rest_framework import status

from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins

from rest_framework import viewsets
from django.shortcuts import get_object_or_404



class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewsSerializers

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        try:
            watchlist = WatchList.objects.get(pk=pk)
        
        except WatchList.DoesNotExist:
            return Response({'errors: Movie not found'}, status = status.HTTP_404_NOT_FOUND)

        serializer.save(movie = watchlist)


class ReviewList(generics.ListAPIView):

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviews.objects.filter(movie = pk)


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers


class StreamPlatFormViewSets(viewsets.ViewSet):
    def list(self, request):
        queryset = StreamPlatForm.objects.all()
        serializer = StreamPlatFormSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatForm.objects.all()
        streamplatf = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatFormSerializers(streamplatf)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = StreamPlatForm.objects.all()
        streamplatf = get_object_or_404(queryset, pk =pk)
        serializer = StreamPlatFormSerializers(streamplatf, data = request.data)

        if serializer.is_valid():
            return serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        
        streamplatf.save()
        return Response()
        



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








 