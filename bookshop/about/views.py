import django.shortcuts
import django.views


class AboutSite(django.views.View):
    def get(self, request, *args, **kwargs):
        return django.shortcuts.render(request, "about.html")
