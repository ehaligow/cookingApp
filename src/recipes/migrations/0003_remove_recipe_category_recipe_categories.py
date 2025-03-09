# Generated by Django 4.2 on 2025-03-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('recipes', '0002_alter_recipe_category_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(to='category.category'),
        ),
    ]
