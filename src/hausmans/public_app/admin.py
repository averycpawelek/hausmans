from django.contrib import admin
from public_app.models import PortfolioProject, PortfolioImage


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}


class ImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'created_at')


admin.site.register(PortfolioProject, ProjectAdmin)
admin.site.register(PortfolioImage, ImageAdmin)
