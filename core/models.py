import os

from django.db import models
from django.urls import reverse

LINK_CHOICES = (
    ("/about", 'O Firmie'),
    ("/offer", 'Oferta'),
    ("/gallery", 'Galeria'),
    ("/contact", 'Kontakt'),
)


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.page, ext)
    return os.path.join("img", filename)


class Paragraph(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default='', blank=True)
    slug = models.SlugField()
    content = models.TextField()
    link = models.CharField(choices=LINK_CHOICES, max_length=50, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-update', kwargs={'pk': self.pk})


class Image(models.Model):
    page = models.CharField(max_length=20, blank=True)
    file = models.FileField(upload_to=content_file_name)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Offer(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    image = models.FileField(upload_to='offers')