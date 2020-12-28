import traceback
import datetime

from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from public_app.forms import ContactUsForm
from public_app.utils import send_email
from public_app.models import PortfolioProject
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


def contact_us_view(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_email(
                request.POST['first_name'],
                request.POST['last_name'],
                request.POST['email_address'],
                request.POST['message']
            )
            form = ContactUsForm()
    else:
        form = ContactUsForm()
    return render(
        request,
        'public_app/contact_us.html',
        {
            'current_page': 'contact-us',
            'form': form
        }
    )


def to_do_view(request):
    return HttpResponse('TODO')


def project_view(request, project_identifier):
    try:
        project = PortfolioProject.objects.get(slug=project_identifier)
    except:
        return HttpResponse("Not found", status=404)
    return HttpResponse(project.name)
