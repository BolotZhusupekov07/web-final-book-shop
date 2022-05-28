from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    class Season(models.TextChoices):
        SPRING = "spring", "Spring"
        SUMMER = "summer", "Summer"
        AUTUMN = "fall", "Fall"
        WINTER = "winter", "Winter"
        SCHOOL_UNIFORM = "school-uniform", "Schoool uniform"

    season = models.CharField(max_length=15, choices=Season.choices)
    name = models.CharField(max_length=250)


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_DEFAULT, default="spring"
    )
    photo_1 = models.ImageField(upload_to="photos/")
    photo_2 = models.ImageField(upload_to="photos/")
    photo_3 = models.ImageField(upload_to="photos/")
    name = models.CharField(max_length=250, db_index=True)
    description = models.TextField()
    material = models.CharField(max_length=250)
    age = models.CharField(max_length=250)
    cost = models.DecimalField(max_digits=10, decimal_places=1)
    size = models.CharField(max_length=250)
    slug = models.SlugField()


class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    total_cost = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
