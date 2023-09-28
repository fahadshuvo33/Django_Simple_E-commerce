from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

class Sub_category(models.Model):
    name = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    
    def __str__(self):
         return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)

    slug = AutoSlugField(populate_from='product_name',unique=True, default=None, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)  # Generate the slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class Blog(models.Model):
    blog_title = models.CharField(max_length=255)
    blog_description = HTMLField()
    image = models.ImageField(upload_to='blog_images/')

    slug = AutoSlugField(populate_from='blog_title',unique=True, default=None, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_title)  # Generate the slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.blog_title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Cart for User: {self.user.username}"
