from django.urls import path
from .views import AboutPage, SupportPage, HomePage, Contact

urlpatterns = [

    path('support/', SupportPage.as_view(), name='support'),
    path('about/', AboutPage.as_view(), name='about'),
    path('', HomePage.as_view(), name='home'),
    path('contact/', Contact.as_view(), name='contact'),


]


