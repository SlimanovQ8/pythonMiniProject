from rest_framework import serializers

from .models import Event


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventAfterCertainDateSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'start_date']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["name"]