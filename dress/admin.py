from django.contrib import admin


from dress.models import Dress


@admin.register(Dress)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image', 'description')

#
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('product',)
#
#
# admin.site.register(Comment, CommentAdmin)


# Register your models here.
