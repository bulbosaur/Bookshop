import django.http
import django.views

class Home(django.views.View):
    def get(self, request, *args, **kwaigs):
        return django.http.HttpResponse('Hello! It is the best bookshop ever')