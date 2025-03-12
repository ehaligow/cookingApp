from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.name}"
        super().save(*args, **kwargs)
