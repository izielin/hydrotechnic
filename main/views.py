from django.shortcuts import render,  redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from .models import Post
import os
from django.urls import reverse
import datetime
from .forms import DocumentForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


def home(request):
    context = {
        'post': Post.objects.filter(category='main_page')

    }
    return render(request, 'main/home.html', context)


def about(request):
    that = datetime.date(1986, 1, 1)
    today = datetime.date.today()
    years = today.year - that.year
    context = {
        'post': Post.objects.filter(category='about'),
        'years': years
    }
    return render(request, 'main/about.html', context)


def offer(request):
    context = {
        'posts': Post.objects.filter(category='offer')
    }
    return render(request, 'main/offer.html', context)


def gallery(request):
    images = os.listdir('./media/documents')
    images = ['/media/documents/' + file for file in images]
    return render(request, 'main/gallery.html', {'images': images})


def post_list(request):
    posts_list = Post.objects.all()
    context = {
        'posts': posts_list
    }
    return render(request, "main/post_list.html", context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.success_url = reverse('post-list')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gallery'))
    else:
        form = DocumentForm()
    return render(request, 'main/file_form.html', {'form': form})