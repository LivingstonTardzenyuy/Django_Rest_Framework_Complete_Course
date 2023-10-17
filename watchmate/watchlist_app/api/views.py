from rest_framework.response import Response
from watchlist_app.models import Movie
from django.http import JsonResponse
from watchlist_app.api.serializers import MovieSerializers 
from rest_framework.decorators import api_view


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def movie_details(request, pk): 
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)