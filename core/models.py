from django.db import models
from django.urls import reverse


class Paragraph(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default='')
    slug = models.SlugField()
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-update', kwargs={'pk': self.pk})
