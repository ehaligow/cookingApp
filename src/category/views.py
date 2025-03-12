from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Category
from .serializers import CategorySerializer


class CategoriesList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
