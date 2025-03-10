from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views.generic.detail import DetailView

from .models import Profile


class SignUp(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect("home")
        return render(request, "registration/signup.html", {"form": form})


class ShowProfilePage(DetailView):
    model = Profile
    template_name = "account/user_profile.html"
    context_object_name = "page_user"
