from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'active']