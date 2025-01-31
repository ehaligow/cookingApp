from rest_framework.views import APIView
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response


class RecipesList(APIView):
    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
