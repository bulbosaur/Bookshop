import django.http
import django.views
import django.shortcuts


class Home(django.views.View):
    def get(self, request, *args, **kwaigs):
        return django.shortcuts.render(request, "home.html")
