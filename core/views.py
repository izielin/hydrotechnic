import os

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from hydrotechnic import settings
from .forms import ParagraphForm, ImageForm, OfferForm
from .models import Paragraph, Image, Offer


def create_paragraph(request):
    form = ParagraphForm(request.GET or None)
    response_data = {}
    if form.is_valid():
        title_form = request.GET.get('title')
        slug = request.GET.get('slug')
        if 'subtitle' in request.GET:
            subtitle_form = request.GET.get('subtitle')
        else:
            subtitle_form = ''
        if 'link' in request.GET:
            link_form = request.GET.get('link')
        else:
            link_form = ''
        content_form = request.GET.get('content')

        try:
            paragraph = Paragraph.objects.get(slug=slug)
            paragraph.title = title_form
            paragraph.subtitle = subtitle_form
            paragraph.slug = slug
            paragraph.content = content_form
            paragraph.link = link_form
            paragraph.save()

        except (ObjectDoesNotExist, IntegrityError):

            paragraph = Paragraph(title=title_form,
                                  subtitle=subtitle_form,
                                  slug=slug,
                                  content=content_form,
                                  link=link_form)
            paragraph.save()

        response_data['title'] = title_form
        response_data['subtitle'] = subtitle_form
        response_data['content'] = content_form

    else:
        pass
    return JsonResponse(response_data)


def create_offer(request):
    data = {}
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.save()
            data = {'is_valid': True, 'title': offer.title, 'image': offer.image.url, 'content': offer.content}
        else:
            data = {'is_valid': False}
    return JsonResponse(data)


def get_context(slug):
    context = {
        'form': ParagraphForm,
    }

    try:
        paragraph = Paragraph.objects.filter(slug__contains=slug).count()
        for p in range(1, int(paragraph) + 1):
            context["paragraph{0}".format(p)] = Paragraph.objects.get(slug=slug + "_{0}".format(p))
    except:
        pass

    return context


def home(request, *args, **kwargs):
    context = get_context("home")
    return render(request, 'core/home.html', context)


def about(request):
    context = get_context("about")
    return render(request, 'core/about.html', context)


def delete_offer(request, pk):
    Offer.objects.filter(id=pk).delete()
    return redirect(request.POST.get('next'))


def offer(request):
    context = get_context("offer")
    context['offer_form'] = OfferForm
    try:
        context["offers"] = Offer.objects.all()
    except:
        pass
    return render(request, 'core/offer.html', context)


def contact(request):
    context = get_context("contact")
    return render(request, 'core/contact.html', context)


def delete_file(request, pk):
    for file in Image.objects.filter(id=pk):
        file.delete()
    root = settings.MEDIA_ROOT + '/images'
    folders = list(os.walk(root))[1:]

    for folder in folders:
        if not folder[2]:
            os.rmdir(folder[0])
    return HttpResponseRedirect(request.POST.get('next'))


class Gallery(View):
    def get(self, request):
        photos_list = Image.objects.filter(page__contains="gallery")
        return render(self.request, 'core/gallery.html', {'photos': photos_list})

    def post(self, request):
        form = ImageForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            page = self.request.POST.get("path").replace("/", "")
            other = Image.objects.filter(page__contains=page).count()
            photo = form.save(commit=False)
            if other < 1:
                photo.page = page
            else:
                photo.page = page + "-" + str(other)
            photo.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
