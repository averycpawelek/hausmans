from django.urls import path
from django.views.static import serve
from .views import (
    home_page_view,
    to_do_view,
    project_view,
    services_view,
    commercial_industrial_roofing_view,
    sheet_metal_view,
    waterjet_view,
    contact_us_view
)

urlpatterns = [
    path("", home_page_view, name="home"),
    path("portfolio", to_do_view, name='portfolio'),
    path("portfolio/<str:project_identifier>", project_view, name='portfolio-project'),
    path("what-we-do", services_view, name='services'),
    path("commercial-industrial-roofing", commercial_industrial_roofing_view, name='commercial-industrial-roofing'),
    path("architectural-sheet-metal", to_do_view, name='architectural-sheet-metal'),
    path("plasma-cutting", to_do_view, name='plasma-cutting'),
    path("sheet-metal-fabrication", sheet_metal_view, name='sheet-metal-fabrication'),
    path("industrial-ventilation", to_do_view, name='industrial-ventilation'),
    path("hvac", to_do_view, name='hvac'),
    path("specialties", to_do_view, name='specialties'),
    path("metal-roofing", to_do_view, name='metal-roofing'),
    path("solar-roofing", to_do_view, name='solar-roofing'),
    path("waterjet-cutting", waterjet_view, name='waterjet-cutting'),
    path("roof-repair", to_do_view, name='roof-repair'),
    path("about-us", to_do_view, name='about-us'),
    path("contact-us", contact_us_view, name='contact-us'),
]

from django.conf import settings

if settings.SERVE_MEDIA_FILES:
    urlpatterns.append(path('media/<path:path>', serve, {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True
    }))
