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
    class Meta:
        model = StreamPlatForm
        fields = "__all__"



# class MovieSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()



#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
        
#         instance.save()
#         return instance 


#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("The name and description must not be the same")
#         return data

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("the name is too short")
#         return value

