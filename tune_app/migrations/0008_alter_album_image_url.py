# Generated by Django 4.0.6 on 2022-07-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tune_app', '0007_album_image_url_artist_image_url_alter_post_artist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image_url',
            field=models.ImageField(upload_to='tune_app'),
        ),
    ]
