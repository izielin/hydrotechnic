from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('main_page_carousel', 'main_page_carousel'),
        ('main_page_services', 'main_page_services'),
        ('footer', 'footer'),
        ('about_content', 'about_content'),
        ('about_main_content', 'about_main_content'),
        ('offer_main_content', 'offer_main_content'),
        ('contact', 'contact'),
    )

    ANCHOR_CHOICES = (
        ('about', 'about'),
        ('offer', 'offer'),
        ('gallery', 'gallery'),
    )

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default='', help_text='Nie jest wymagane')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='')
    anchor = models.CharField(max_length=100, choices=ANCHOR_CHOICES, default='')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-update', kwargs={'pk': self.pk})


class Document(models.Model):
    name = models.CharField(max_length=100, unique=True)
    document = models.FileField(upload_to='documents/')
