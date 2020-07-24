from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('offer/', views.offer, name='offer'),
    path('contact/', views.contact, name='contact'),
    url(r'^ajax/create/$', views.create_paragraph, name='create'),
    url(r'^ajax/create/offer/$', views.create_offer, name='create_offer'),
    url(r'^ajax/create/address/$', views.create_address, name='create_address'),
    url(r'^ajax/create/box/$', views.create_box, name='create_box'),
    url(r'^gallery/$', views.Gallery.as_view(), name='gallery'),
    path('upload/<int:pk>/', views.delete_file, name='upload_delete'),
    path('offer/delete/<int:pk>/', views.delete_offer, name='offer_delete'),
    path('box/delete/<int:pk>/', views.delete_box, name='box_delete'),
    url(r'^clear/$', views.clear_all, name='clear'),

]
