# Generated by Django 5.0 on 2024-04-27 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cart_cartitems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItems',
            new_name='CartItem',
        ),
    ]
