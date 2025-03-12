from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status


class RecipesList(ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        categories = self.request.query_params.getlist('categories')
        if categories:
            for category in categories:
                queryset = queryset.filter(categories__name__iexact=category)
        return queryset


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
