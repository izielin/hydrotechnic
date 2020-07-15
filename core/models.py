from django.db import models
from django.urls import reverse

LINK_CHOICES = (
    ("/about", 'O Firmie'),
    ("/offer", 'Oferta'),
    ("/gallery", 'Galeria'),
    ("/contact", 'Kontakt'),
)


class Paragraph(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default='')
    slug = models.SlugField()
    content = models.TextField()
    link = models.CharField(choices=LINK_CHOICES, max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-update', kwargs={'pk': self.pk})
