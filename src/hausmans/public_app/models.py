from django.db import models


class PortfolioProject(models.Model):
    name = models.CharField(max_length=1000)
    thumbnail_image = models.ImageField(upload_to='portfolio_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PortfolioImage(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
