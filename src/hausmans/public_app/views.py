import traceback
import datetime

from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.forms.models import inlineformset_factory
from django.contrib import messages


def home_page_view(request):
    return render(request, 'public_app/home.html')


def services_view(request):
    return render(request, 'public_app/services.html')


def commercial_industrial_roofing_view(request):
    return render(request, 'public_app/commercial-industrial-roofing.html')


def to_do_view(request):
    return HttpResponse('TODO')


def to_do_project_view(request, project_identifier):
    return HttpResponse(project_identifier)
