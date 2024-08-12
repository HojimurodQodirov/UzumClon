from django.urls import path
from .views import ProductListView, ProductImageListView, HeaderAdsListView, CategoryListView, MiddleCategoryListView, \
    BranchListView, VacancyListView, ConnectWithUsListView, QuestionListView, ForSellerListView, \
    EntranceForSellerListView, PrivacyPolicyListView, SocialMediaListView, CartListView, AddToCartView, \
    AddToFavoriteView, FavoriteListView, ProductSearchView, ReviewCreateView, RemoveFromCartView, PurchaseListView, \
    RemoveFromFavoriteView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product-images/', ProductImageListView.as_view(), name='product-image-list'),
    path('header-ads/', HeaderAdsListView.as_view(), name='header-ads-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('middle-categories/', MiddleCategoryListView.as_view(), name='middle-category-list'),
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('vacancies/', VacancyListView.as_view(), name='vacancy-list'),
    path('connect-with-us/', ConnectWithUsListView.as_view(), name='connect-with-us-list'),
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('for-sellers/', ForSellerListView.as_view(), name='for-seller-list'),
    path('entrance-for-sellers/', EntranceForSellerListView.as_view(), name='entrance-for-seller-list'),
    path('privacy-policies/', PrivacyPolicyListView.as_view(), name='privacy-policy-list'),
    path('social-media/', SocialMediaListView.as_view(), name='social-media-list'),
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('favorite/', FavoriteListView.as_view(), name='cart-list'),
    path('favorite/add/', AddToFavoriteView.as_view(), name='add-to-cart'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('favorite/remove/', RemoveFromFavoriteView.as_view(), name='remove-from-cart'),
    path('purchases/', PurchaseListView.as_view(), name='purchase-list')
]
