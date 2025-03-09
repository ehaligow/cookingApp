from django.db import models
from category.models import Category


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField(max_length=500)
    instruction = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'
