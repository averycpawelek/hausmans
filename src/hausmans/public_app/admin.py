from django.contrib import admin
from public_app.models import PortfolioProject, PortfolioImage


class ImageInline(admin.TabularInline):
    model = PortfolioImage
    verbose_name = "Additional Image"
    verbose_name_plural = "Additional Images"


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageInline]


admin.site.register(PortfolioProject, ProjectAdmin)
