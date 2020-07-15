import datetime
import os

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View

from .models import Paragraph
from .forms import ParagraphForm


def create_paragraph(request):
    print("sanity check")
    for key, value in request.GET.items():
        print('Key: %s' % (key))
        print('Value %s' % (value))

    form = ParagraphForm(request.GET or None)
    response_data = {}
    if form.is_valid():
        title_form = request.GET.get('title')
        slug = request.GET.get('slug')
        if 'subtitle' in request.GET:
            subtitle_form = request.GET.get('subtitle')
        else:
            subtitle_form = ''
        content_form = request.GET.get('content')
        try:
            print("sanity check I")
            paragraph = Paragraph.objects.get(slug=slug)
            paragraph.title = title_form
            paragraph.subtitle = subtitle_form
            paragraph.slug = slug
            paragraph.content = content_form
            paragraph.save()
            print("sanity check II")

        except (ObjectDoesNotExist, IntegrityError):
            print("sanity check III")

            paragraph = Paragraph(title=title_form,
                                  subtitle=subtitle_form,
                                  slug=slug,
                                  content=content_form)
            paragraph.save()

        response_data['title'] = title_form
        response_data['subtitle'] = subtitle_form
        response_data['content'] = content_form

    else:
        messages.warning(request, "Please fill in the required fields")
    return JsonResponse(response_data)


def home(request, *args, **kwargs):
    context = {
        'form': ParagraphForm,
    }

    try:
        home_paragraph = Paragraph.objects.filter(slug__contains="home").count()
        for p in range(1, int(home_paragraph) + 1):
            context["paragraph{0}".format(p)] = Paragraph.objects.get(slug="home_{0}".format(p))
    except:
        pass

    return render(request, 'core/home.html', context)


def about(request):
    that = datetime.date(1986, 1, 1)
    today = datetime.date.today()
    years = today.year - that.year
    context = {
        'years': years
    }
    return render(request, 'core/about.html', context)


def offer(request):
    return render(request, 'core/offer.html')


def gallery(request):
    images = os.listdir('./media/documents')
    images = ['/media/documents/' + file for file in images]
    return render(request, 'core/gallery.html', {'images': images})
