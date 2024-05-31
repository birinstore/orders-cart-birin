from django.contrib import admin

from shoes.models import Shoes


@admin.register(Shoes)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image', 'description')

#
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('product',)
#
#
# admin.site.register(Comment, CommentAdmin)

