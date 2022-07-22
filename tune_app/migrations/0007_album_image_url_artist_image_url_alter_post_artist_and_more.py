# Generated by Django 4.0.6 on 2022-07-08 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tune_app', '0006_alter_post_artist_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image_url',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='artist',
            name='image_url',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='tune_app.artist'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]