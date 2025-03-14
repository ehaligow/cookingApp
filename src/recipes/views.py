from rest_framework.views import APIView
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status


class RecipesList(APIView):
    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)


class RecipeDetailView(APIView):
    def get(self, request, product_slug, format=None):
        try:
            recipe = Recipe.objects.get(slug=product_slug)
        except Recipe.DoesNotExist:
            raise NotFound(detail="Recipe not found")
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)


class RecipeCeateView(APIView):
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
