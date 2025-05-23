# Generated by Django 5.2 on 2025-05-12 12:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_closing_time_store_opening_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='name',
            field=models.CharField(default='五倍學院', max_length=100),
        ),
        migrations.AddField(
            model_name='store',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
