# Generated by Django 3.1 on 2020-12-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_app', '0003_auto_20201228_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioproject',
            name='slug',
            field=models.SlugField(default='', verbose_name='URL'),
        ),
    ]
