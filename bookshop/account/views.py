import django.contrib
import django.contrib.auth
import django.contrib.auth.forms
import django.shortcuts
import django.views


class SignUp(django.views.View):
    def get(self, request, *args, **kwargs):
        if request.method == "POST":
            form = django.contrib.auth.forms.UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                django.contrib.auth.login(request, user)
                return django.shortcuts.redirect("home")
        else:
            form = django.contrib.auth.forms.UserCreationForm()
        return django.shortcuts.render(
            request, "registration/signup.html", context={"form": form}
        )
