from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatForm
from django.http import JsonResponse
from watchlist_app.api.serializers import WatchListSerializers, StreamPlatFormSerializers 
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from rest_framework import status

from rest_framework.views import APIView




class StreamPlatFormAV(APIView):
    def get(self, request):
        streamPlatForm = StreamPlatForm.objects.all()
        serializer = StreamPlatFormSerializers(streamPlatForm, many = True)
        return Response(serializer.data)


    def post(self, request):
        serializer = StreamPlatFormSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class StreamPlatFormDetailAV(APIView):
    def get(self, request, pk):
        try:
            streamPlatForm = StreamPlatForm.objects.get(pk=pk)
        except StreamPlatForm.DoesNotExists:
            return Response({'error: Movie not found'}, status = status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatForm(streamPlatForm) 

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










# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializers(movies, many=True)

#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk): 
#     if request.method == 'GET':

#         try:
#             movie = Movie.objects.get(pk=pk)

#         except Movie.DoesNotExist:
#             return Response({'Error: Movie not found'}, status= status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializers(movie)
#         return Response(serializer.data, status = status.HTTP_200_OK)
    

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializers(movie, data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    