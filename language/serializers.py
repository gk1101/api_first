from rest_framework import serializers
from .models import Language

# A serializer translates to and from JSON for the API

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Language
        fields= ("name","paradigm")