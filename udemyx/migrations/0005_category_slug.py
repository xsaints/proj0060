# Generated by Django 2.1.2 on 2018-10-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udemyx', '0004_auto_20181018_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=200), max_length=500),
        ),
    ]
