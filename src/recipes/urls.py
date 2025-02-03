from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('recipes/', views.RecipesList.as_view()),
    path("recipes/<slug:product_slug>/", views.RecipeDetailView.as_view()),
]
