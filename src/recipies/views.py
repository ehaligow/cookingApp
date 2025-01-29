from rest_framework.views import APIView
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response


class RecipiesList(APIView):
    def get(self, request, format=None):
        recipies = Recipe.objects.all()
        serializer = RecipeSerializer(recipies, many=True)
        return Response(serializer.data)
