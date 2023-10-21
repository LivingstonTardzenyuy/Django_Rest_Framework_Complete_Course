from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatForm


class WatchListSerializers(serializers.ModelSerializer):


    len_name = serializers.SerializerMethodField()            #custom serializer field.

    class Meta:
        model = WatchList 
        fields = "__all__"



    def get_len_name(self, object):
        length = len(object.name)
        return length

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('the name and description should be different')
        return data 

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('the name length is small')
        else:
            return value

                

class StreamPlatFormSerializers(serializers.ModelSerializer):
    len_names = serializers.SerializerMethodField()
    class Meta:
        model = StreamPlatForm
        fields = "__all__"


    def get_len_names(self, data):
        return len(data.name)

    def validate_about(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('The content of about is too short')
        return value

    
    def validate(self, data):
        if data['name'] == data['about']:
            raise serializers.ValidationError('The name and about must be different')
        return data