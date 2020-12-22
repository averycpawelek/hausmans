import traceback
import datetime

from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.forms.models import inlineformset_factory
from django.contrib import messages


def home_page_view(request):
    return render(request, 'public_app/home.html', {'current_page': 'home'})


def services_view(request):
    return render(request, 'public_app/services.html', {'current_page': 'services'})


def commercial_industrial_roofing_view(request):
    return render(request, 'public_app/commercial-industrial-roofing.html', {'current_page': 'commercial-industrial-roofing'})


def sheet_metal_view(request):
    return render(request, 'public_app/sheet_metal_fabrication.html',
                  {'current_page': 'sheet-metal-fabrication'})


def waterjet_view(request):
    return render(request, 'public_app/waterjet_cutting.html',
                  {'current_page': 'waterjet-cutting'})

def to_do_view(request):
    return HttpResponse('TODO')


def to_do_project_view(request, project_identifier):
    return HttpResponse(project_identifier)
