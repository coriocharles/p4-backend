# Generated by Django 4.0.6 on 2022-07-13 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tune_app', '0014_alter_post_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='avg_rating',
            field=models.IntegerField(default=0),
        ),
    ]