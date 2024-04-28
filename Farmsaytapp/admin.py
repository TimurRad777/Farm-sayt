from django.contrib import admin
from .models import Post, Product


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}

admin.site.register(Post,SlugAdmin)
admin.site.register(Product,SlugAdmin)