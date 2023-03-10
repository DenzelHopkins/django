from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import NameSerializer
from .models import Name

class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all().order_by('last_name')
    serializer_class = NameSerializer