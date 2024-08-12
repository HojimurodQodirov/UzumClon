from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, ProductImage, HeaderAds, Category, MiddleCategory, Branch, Vacancy, ConnectWithUs, \
    Question, ForSeller, EntranceForSeller, PrivacyPolicy, SocialMedia, Cart, Favorite, Review, Purchase


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'header_image', 'title', 'slug', 'seller', 'count', 'price', 'description', 'category']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product', 'image']


class HeaderAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderAds
        fields = ['images']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'parent']


class MiddleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MiddleCategory
        fields = ['title']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['category', 'location', 'title', 'description']


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['category', 'title', 'description', 'telegram', 'email']


class ConnectWithUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectWithUs
        fields = ['category', 'title', 'description', 'telegram', 'phone_number']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['category', 'title', 'text']


class ForSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForSeller
        fields = ['category', 'url']


class EntranceForSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntranceForSeller
        fields = ['category', 'url']


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ['text']


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['telegram', 'instagram', 'facebook', 'youtube']


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['user', 'products', 'created_at', 'updated_at']


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Product does not exist.")
        return value

    def create(self, validated_data):
        cart, created = Cart.objects.get_or_create(user=self.context['request'].user)
        product = Product.objects.get(id=validated_data['product_id'])
        cart.products.add(product)
        return cart


class FavoriteSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Favorite
        fields = ['user', 'products', 'created_at', 'updated_at']


class AddToFavoriteSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Product does not exist.")
        return value

    def create(self, validated_data):
        favorite, created = Favorite.objects.get_or_create(user=self.context['request'].user)
        product = Product.objects.get(id=validated_data['product_id'])
        favorite.products.add(product)
        return favorite


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment', 'created_at']


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'



