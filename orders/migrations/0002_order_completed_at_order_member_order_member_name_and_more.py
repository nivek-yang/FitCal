# Generated by Django 5.2 on 2025-05-11 15:42

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_member_phone_number'),
        ('orders', '0001_initial'),
        ('products', '0007_alter_product_calories_alter_product_price'),
        ('stores', '0002_store_closing_time_store_opening_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.member'),
        ),
        migrations.AddField(
            model_name='order',
            name='member_name',
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='orders', through='orders.OrderItem', to='products.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stores.store'),
        ),
        migrations.AddField(
            model_name='order',
            name='store_name',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='subtotal',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
