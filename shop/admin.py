from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Category, Product, Cart, CartItem


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register([Product, Cart, CartItem])
