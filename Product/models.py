from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        db_table = "Category"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description =models.TextField()
    image = models.ImageField(upload_to = "product")
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    class Meta:
        db_table = "Product"
