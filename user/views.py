from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.contrib import messages

from .forms import RegisterForm
from django.contrib.auth.models import User

from .decorators import anonymous_required


def create_account(request, form):
    print("check")
    amountOfUsers = User.objects.count()
    print("check II")

    if amountOfUsers < 1:
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            print("check III")
            return redirect("login")
    else:
        print("check IV")
        messages.warning(request,
                         'Osiągnięto limit zalogowanych użytkowników, skontaktuj się z administratorem strony.')
    return render(request, 'core/messages.html')


@method_decorator(anonymous_required, name='dispatch')
class SignUpView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'registration/signup.html'

    def form_valid(self, form, **kwargs):
        return create_account(self.request, form)
