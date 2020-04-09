from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer
# Create your views here.

# viewsets.ModelViewSet basically saves from defining what will happen
# everytime there is a GET< POST< DELETE etc type of request
# we don't need to define them
class LanguageView(viewsets.ModelViewSet):
    queryset= Language.objects.all()
    serializer_class= LanguageSerializer

