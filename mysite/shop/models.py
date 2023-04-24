from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=200)

class Product(models.Model):
    product_name = models.CharField(max_length=300)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)

