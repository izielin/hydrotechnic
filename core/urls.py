from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('o_firmie/', views.about, name='about'),
    path('oferta/', views.offer, name='offer'),
    path('kontakt/', views.contact, name='contact'),
    url(r'^utworz/paragraf/$', views.create_paragraph, name='create'),
    url(r'^utworz/oferte/$', views.create_offer, name='create_offer'),
    url(r'^utworz/adres/$', views.create_address, name='create_address'),
    url(r'^utworz/pudelko/$', views.create_box, name='create_box'),
    url(r'^galeria/$', views.Gallery.as_view(), name='gallery'),
    path('dodaj_zdjecie/<int:pk>/', views.delete_file, name='upload_delete'),
    path('usun/oferte/<int:pk>/', views.delete_offer, name='offer_delete'),
    path('usun/pudelko/<int:pk>/', views.delete_box, name='box_delete'),
    url(r'^wyczysc/$', views.clear_all, name='clear'),

]
