from rest_framework import generics, status
from user.models import Seller
from .models import Product, ProductImage, HeaderAds, Category, MiddleCategory, Branch, Vacancy, ConnectWithUs, \
    Question, ForSeller, EntranceForSeller, PrivacyPolicy, SocialMedia, Cart, Favorite, Review, Purchase
from .serializers import ProductSerializer, ProductImageSerializer, HeaderAdsSerializer, CategorySerializer, \
    MiddleCategorySerializer, BranchSerializer, VacancySerializer, ConnectWithUsSerializer, QuestionSerializer, \
    ForSellerSerializer, EntranceForSellerSerializer, PrivacyPolicySerializer, SocialMediaSerializer, CartSerializer, \
    AddToCartSerializer, FavoriteSerializer, AddToFavoriteSerializer, ReviewSerializer, PurchaseSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageListView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class HeaderAdsListView(generics.ListAPIView):
    queryset = HeaderAds.objects.all()
    serializer_class = HeaderAdsSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MiddleCategoryListView(generics.ListAPIView):
    queryset = MiddleCategory.objects.all()
    serializer_class = MiddleCategorySerializer


class BranchListView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class ConnectWithUsListView(generics.ListAPIView):
    queryset = ConnectWithUs.objects.all()
    serializer_class = ConnectWithUsSerializer


class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ForSellerListView(generics.ListAPIView):
    queryset = ForSeller.objects.all()
    serializer_class = ForSellerSerializer


class EntranceForSellerListView(generics.ListAPIView):
    queryset = EntranceForSeller.objects.all()
    serializer_class = EntranceForSellerSerializer


class PrivacyPolicyListView(generics.ListAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer


class SocialMediaListView(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class AddToCartView(generics.GenericAPIView):
    serializer_class = AddToCartSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart = serializer.save()
        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)


class FavoriteListView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class AddToFavoriteView(generics.GenericAPIView):
    serializer_class = AddToFavoriteSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        favorite = serializer.save()
        return Response(FavoriteSerializer(favorite).data, status=status.HTTP_201_CREATED)


class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'title']

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Product.objects.filter(title__icontains=query)


class RemoveFromCartView(generics.GenericAPIView):
    serializer_class = AddToCartSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart = Cart.objects.get(user=request.user)
        product = Product.objects.get(id=serializer.validated_data['product_id'])
        cart.products.remove(product)
        return Response(CartSerializer(cart).data, status=status.HTTP_204_NO_CONTENT)


class RemoveFromFavoriteView(generics.GenericAPIView):
    serializer_class = AddToFavoriteSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        favorite = Favorite.objects.get(user=request.user)
        product = Product.objects.get(id=serializer.validated_data['product_id'])
        favorite.products.remove(product)
        return Response(FavoriteSerializer(favorite).data, status=status.HTTP_204_NO_CONTENT)



class PurchaseListView(generics.ListAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        seller = Seller.objects.get(user=user)
        return Purchase.objects.filter(user=seller)


