# Generated by Django 4.0.6 on 2022-07-05 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tune_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.ManyToManyField(to='tune_app.genre'),
        ),
    ]
