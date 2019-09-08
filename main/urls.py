from django.urls import path
from .views import (
    PostUpdateView,
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('offer/', views.offer, name='offer'),
    path('gallery/', views.gallery, name='gallery'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post_list/', views.post_list, name='post-list'),
    path('upload/', views.model_form_upload, name='upload'),
]