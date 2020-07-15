from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('offer/', views.offer, name='offer'),
    path('gallery/', views.gallery, name='gallery'),
    url(r'^ajax/create/$', views.create_paragraph, name='create'),
]
