from django.db import models
from category.models import Category
# Create your models here.

class Product(models.Model):
    name  = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(max_length=50, unique = True)
    description = models.TextField(max_length=500,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'photoes/products')
    stock = models.IntegerField(default = 100)
    is_available = models.BooleanField(default = True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


    def _str_(self) -> str:
        return self.name

