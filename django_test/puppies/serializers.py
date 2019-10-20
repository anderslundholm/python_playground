from rest_framework import serializers
from puppies.models import Puppy


class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = ('id', 'name', 'age', 'breed', 'color', 'created_at', 'updated_at')
