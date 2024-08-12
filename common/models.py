from django.db import models
from user.models import Seller
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    header_image = models.URLField()
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.URLField()

    def __str__(self):
        return self.product.title


class HeaderAds(models.Model):
    images = models.URLField()

    def __str__(self):
        return self.images


class MiddleCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Branch(models.Model):
    category = models.ForeignKey(MiddleCategory, on_delete=models.CASCADE)
    location = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    category = models.ForeignKey(MiddleCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    telegram = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.title


class ConnectWithUs(models.Model):
    category = models.ForeignKey(MiddleCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    telegram = models.URLField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Question(models.Model):
    category = models.ForeignKey(MiddleCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class ForSeller(models.Model):
    category = models.ForeignKey(MiddleCategory, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url


class EntranceForSeller(models.Model):
    category = models.ForeignKey(MiddleCategory, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url


class PrivacyPolicy(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class SocialMedia(models.Model):
    telegram = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField   ()
    youtube = models.URLField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InstalledApp(models.Model):
    appstore_url = models.URLField()
    playmarket_url = models.URLField()


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(Seller, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Purchase(models.Model):
    user = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)