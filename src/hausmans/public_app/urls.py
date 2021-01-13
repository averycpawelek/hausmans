from django.urls import path
from django.views.static import serve
from .views import (
    home_page_view,
    portfolio_view,
    project_view,
    services_view,
    commercial_industrial_roofing_view,
    sheet_metal_view,
    waterjet_view,
    contact_us_view
)

urlpatterns = [
    path("", home_page_view, name="home"),
    path("portfolio/", portfolio_view, name='portfolio'),
    path("portfolio/<str:project_identifier>/", project_view, name='portfolio-project'),
    path("what-we-do/", services_view, name='services'),
    path("commercial-industrial-roofing/", commercial_industrial_roofing_view, name='commercial-industrial-roofing'),
    path("sheet-metal-fabrication/", sheet_metal_view, name='sheet-metal-fabrication'),
    path("waterjet-cutting/", waterjet_view, name='waterjet-cutting'),
    path("contact-us/", contact_us_view, name='contact-us'),
]

from django.conf import settings

if settings.SERVE_MEDIA_FILES:
    urlpatterns.append(path('media/<path:path>/', serve, {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True
    }))
