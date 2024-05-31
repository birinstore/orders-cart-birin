from django.contrib import admin

from products.models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image', 'description')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('product',)


admin.site.register(Comment, CommentAdmin)

