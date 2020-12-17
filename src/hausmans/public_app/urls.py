from django.urls import path
from .views import (
    home_page_view,
    to_do_view,
)

urlpatterns = [
    path("", home_page_view, name="home"),
    path("portfolio", to_do_view, name='portfolio'),
    path("what-we-do", to_do_view, name='services'),
    path("commercial-industrial-roofing", to_do_view, name='commercial-industrial-roofing'),
    path("architectural-sheet-metal", to_do_view, name='architectural-sheet-metal'),
    path("plasma-cutting", to_do_view, name='plasma-cutting'),
    path("sheet-metal-fabrication", to_do_view, name='sheet-metal-fabrication'),
    path("industrial-ventilation", to_do_view, name='industrial-ventilation'),
    path("hvac", to_do_view, name='hvac'),
    path("specialties", to_do_view, name='specialties'),
    path("metal-roofing", to_do_view, name='metal-roofing'),
    path("solar-roofing", to_do_view, name='solar-roofing'),
    path("waterjet-cutting", to_do_view, name='waterjet-cutting'),
    path("roof-repair", to_do_view, name='roof-repair'),
    path("about-us", to_do_view, name='about-us'),
    path("contact-us", to_do_view, name='contact-us'),
]
