import traceback
import datetime

from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.forms.models import inlineformset_factory
from django.contrib import messages


def home_page_view(request):
    return render(request, 'public_app/home.html')


def to_do_view(request):
    return HttpResponse('TODO')
