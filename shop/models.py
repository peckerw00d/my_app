import uuid

from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        db_table = 'app_category'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    count = models.PositiveIntegerField(default=0)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='products', null=True, blank=True)
    slug = models.SlugField(default=None, blank=True, null=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='img', default='', null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    description = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=0)
