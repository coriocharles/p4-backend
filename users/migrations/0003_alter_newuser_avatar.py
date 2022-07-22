# Generated by Django 4.0.6 on 2022-07-13 19:28

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_newuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=users.models.upload_to, verbose_name='Image'),
        ),
    ]