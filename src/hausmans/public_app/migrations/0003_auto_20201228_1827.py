# Generated by Django 3.1 on 2020-12-28 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_app', '0002_auto_20201228_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioproject',
            name='thumbnail_image',
            field=models.ImageField(upload_to='portfolio_images'),
        ),
    ]
