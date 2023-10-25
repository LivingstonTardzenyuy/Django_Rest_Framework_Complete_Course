from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class StreamPlatForm(models.Model):
    name = models.CharField(max_length = 30)
    about = models.CharField(max_length = 150)
    website = models.URLField(max_length = 100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatForm, on_delete = models.CASCADE, related_name = "watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length = 200, null=True)
    active = models.BooleanField(default=True)
    movie = models.ForeignKey(WatchList, on_delete = models.CASCADE, related_name = 'reviews')
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)


    def __str__(self):
        return str(self.rating) + " - " + self.movie.title


# class ReviewCreate(generics.CreateAPIView):
#     serializer_class = ReviewsSerializers 

#     def perform_create(self, serializer):
#         pk = self.kwargs.get('pk')
#         try:
#             watchlist = Watchlist.objects.get(pk=pk)
#         except WatchList.DoesNotExists:
#             return Response({'error: Movie not found'}, status = status.HTTP_404_NOT_FOUND)
        
#         serializer