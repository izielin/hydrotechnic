import datetime
import os

from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from hydrotechnic import settings
from .forms import ParagraphForm, ImageForm, OfferForm, AddressForm, BoxForm
from .models import Paragraph, Image, Offer, Address, Box


def create_paragraph(request):
    response_data = {}
    slug = request.POST.get('slug')

    try:
        instance = Paragraph.objects.get(slug=slug)
        form = ParagraphForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            paragraph = form.save(commit=False)
            paragraph.slug = slug
            paragraph.save()

    except (ObjectDoesNotExist, IntegrityError):

        form = ParagraphForm(request.POST, request.FILES)
        if form.is_valid():
            paragraph = form.save(commit=False)
            paragraph.slug = slug
            paragraph.save()

    response_data['title'] = request.POST.get('title')
    response_data['subtitle'] = request.POST.get('subtitle')
    response_data['content'] = request.POST.get('content')

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


def create_address(request):
    print("start")
    form = AddressForm(request.GET or None)
    print(form)
    print(form.is_valid())
    if form.is_valid():
        street = request.GET.get('street')
        cityName = request.GET.get('cityName')
        phone = request.GET.get('phone')
        email = request.GET.get('email')

        try:
            print("I")
            address = Address.objects.get()
            address.street = street
            address.cityName = cityName
            address.phone = phone
            address.email = email
            address.save()

        except (ObjectDoesNotExist, IntegrityError):
            print("II")
            address = Address(street=street, cityName=cityName, phone=phone, email=email)
            address.save()

        address_data = {'is_valid': True, 'street': street, 'city': cityName, 'phone': phone, 'email': email}
    else:
        address_data = {'is_valid': False}
    return JsonResponse(address_data)


def delete_box(request, pk):
    Box.objects.filter(id=pk).delete()
    return redirect(request.POST.get('next'))


def create_box(request):
    form = BoxForm(request.GET or None)
    if request.GET.get('experience') != 'on':
        experience = False
    else:
        experience = True

    if form.is_valid():
        title = request.GET.get('title')
        amount = request.GET.get('amount')
        experience = experience
        box = Box(title=title, amount=amount, experience=experience)
        box.save()
        address_data = {'is_valid': True, 'title': title, 'amount': amount, 'experience': experience}
    else:
        address_data = {'is_valid': False}
    return JsonResponse(address_data)


def get_context(slug):
    context = {
        'form': ParagraphForm,
    }

    try:
        paragraph = Paragraph.objects.filter(slug__contains=slug).count()
        print(paragraph)
        for p in range(1, int(paragraph) + 1):
            context["paragraph{0}".format(p)] = Paragraph.objects.get(slug=slug + "_{0}".format(p))
    except:
        pass

    return context


def home(request, *args, **kwargs):
    context = get_context("home")
    print(context)
    return render(request, 'core/home.html', context)


def about(request):
    context = get_context("about")
    context['box_form'] = BoxForm
    context['boxes'] = Box.objects.all()
    context['date'] = int(datetime.date.today().year - datetime.date(1986, 1, 1).year)
    return render(request, 'core/about.html', context)


def clear_all(request):
    Model = apps.get_model('core', request.POST.get('model'))
    for item in Model.objects.all():
        try:
            item.file.delete()
            item.delete()
        except AttributeError:
            item.delete()
    return redirect(request.POST.get('next'))


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
    context = {
        'form': AddressForm,
    }
    try:
        context['address'] = Address.objects.get()
    except ObjectDoesNotExist:
        context['address'] = ''
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
