from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages

from dress.models import Dress
from products.models import Product
from shoes.models import Shoes


# Create your views here.
class AboutPage(TemplateView):
    template_name = 'pages/about.html'


class SupportPage(TemplateView):
    template_name = 'pages/support.html'


class HomePage(TemplateView):
    template_name = 'home.html'


class Contact(TemplateView):
    template_name = 'pages/contact.html'
