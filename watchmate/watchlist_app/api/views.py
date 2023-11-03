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
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from watchlist_app.api.permission import IsAdminOrReadOnly, IsReviewUserOrReadOnly
class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewsSerializers

    def get_queryset(self):
        return Reviews.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'errors: Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        review_user = self.request.user 
        review_queryset = Reviews.objects.filter(movie=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError('You have already reviewed this movie.')

        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating * watchlist.number_rating + serializer.validated_data['rating']) / (watchlist.number_rating + 1)
        watchlist.number_rating += 1
        watchlist.save()
        serializer.save(movie=watchlist, review_user=review_user)
        
class ReviewList(generics.ListAPIView):
    serializer_class = ReviewsSerializers
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviews.objects.filter(movie = pk)


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    permission_classes = [IsReviewUserOrReadOnly]

class StreamPlatFormViewSets(viewsets.ModelViewSet):
    queryset = StreamPlatForm.objects.all()
    serializer_class = StreamPlatFormSerializers
    permission_classes = [IsAdminOrReadOnly]


# class StreamPlatFormViewSets(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatForm.objects.all()
#         serializer = StreamPlatFormSerializers(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatForm.objects.all()
#         streamplatf = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatFormSerializers(streamplatf)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         queryset = StreamPlatForm.objects.all()
#         streamplatf = get_object_or_404(queryset, pk =pk)
#         serializer = StreamPlatFormSerializers(streamplatf, data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        
#         streamplatf.save()
#         return Response()
        

#     def create(self, request, *args, **kwargs):
#         serializer = StreamPlatFormSerializers(data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
        
#         else:
#             return Response({'error: error'}, status = status.HTTP_400_BAD_REQUEST)

class StreamPlatFormAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
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
    permission_classes = [IsAdminOrReadOnly]
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




class WatchListAV(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    
    serializer_class = WatchListSerializers 

    def perforn_create(self, serializer):
        pk = self.kwargs.get('pk')
        try:
            streamplt = StreamPlatForm.objects.get(pk=pk)
        except StreamPlatForm.DoesNotExist:
            return Response({'error: Streamplatform does not exist'}, status = status.HTTP_400_BAD_REQUEST)
        serializer.save(platform = streamplt)

    def get_queryset(self):
        serializer_class = WatchListSerializers 

        return WatchList.objects.filter()

class WatchListDetailAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
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








 