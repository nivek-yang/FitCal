# Generated by Django 5.2 on 2025-05-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_name_member_user_alter_member_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
