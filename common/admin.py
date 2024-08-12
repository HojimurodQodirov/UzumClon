from django.contrib import admin
from .models import Product, ProductImage, HeaderAds, Category, MiddleCategory, Branch, Vacancy, ConnectWithUs, \
    Question, ForSeller, EntranceForSeller, PrivacyPolicy, SocialMedia, Cart, Favorite, InstalledApp, Review, Purchase

admin.site.register(ProductImage)
admin.site.register(HeaderAds)
admin.site.register(Category)
admin.site.register(MiddleCategory)
admin.site.register(Branch)
admin.site.register(Vacancy)
admin.site.register(ConnectWithUs)
admin.site.register(Question)
admin.site.register(ForSeller)
admin.site.register(EntranceForSeller)
admin.site.register(PrivacyPolicy)
admin.site.register(SocialMedia)
admin.site.register(Cart)
admin.site.register(Favorite)
admin.site.register(InstalledApp)
admin.site.register(Review)
admin.site.register(Purchase)


class ProductImageline(admin.StackedInline):
    model = ProductImage
    extra = 1



@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageline]
    list_display = ['title']

    def detailed_info_url(self, obj):
        return obj.get_detailed_info_url()

    detailed_info_url.short_description = 'product_image'