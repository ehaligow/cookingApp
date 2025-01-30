from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('recipies/', views.RecipiesList.as_view()),
    path("recipies/<slug:product_slug>/", views.RecipeDetailView.as_view()),
]
