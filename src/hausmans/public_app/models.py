from django.db import models
from django.template.defaultfilters import slugify


class PortfolioProject(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(default='', verbose_name='URL')
    thumbnail_image = models.ImageField(upload_to='portfolio_images', verbose_name='Main Image')
    project_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PortfolioImage(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
