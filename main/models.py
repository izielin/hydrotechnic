from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('main_page', 'main_page'),
        ('about', 'about'),
        ('offer', 'offer'),
        ('contact', 'contact'),
    )

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default='', help_text='Nie jest wymagane')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-update', kwargs={'pk': self.pk})


class Document(models.Model):
    name = models.CharField(max_length=100, unique=True)
    document = models.FileField(upload_to='documents/')
