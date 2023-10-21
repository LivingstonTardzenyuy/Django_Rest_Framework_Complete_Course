from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatForm


class WatchListSerializers(serializers.ModelSerializer):


    len_title = serializers.SerializerMethodField()            #custom serializer field.

    class Meta:
        model = WatchList 
        fields = "__all__"



    def get_len_title(self, object):
        length = len(object.title)
        return length

    def validate(self, data):
        if data['title'] == data['storyline']:
            raise serializers.ValidationError('the title and description should be different')
        return data 

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('the title length is small')
        else:
            return value

                

class StreamPlatFormSerializers(serializers.ModelSerializer):
    watchlist = WatchListSerializers(many = True, read_only = True)
    # watchlist = serializers.StringRelatedField(many = True, read_only = True)
    # len_names = serializers.SerializerMethodField()

    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-details'
    # )
    class Meta:
        model = StreamPlatForm
        fields = "__all__"


    # def get_len_names(self, data):
    #     return len(data.name)

    def validate_about(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('The content of about is too short')
        return value

    
    def validate(self, data):
        if data['name'] == data['about']:
            raise serializers.ValidationError('The name and about must be different')
        return data