import django.http
import django.views
import django.shortcuts

import catalog.models

class Home(django.views.View):
    def get(self, request, *args, **kwaigs):
        popular_products = catalog.models.Book.objects.all().order_by("id")[:3]
        return django.shortcuts.render(
            request,
            "index.html",
            context={
                'popular_products': popular_products
            }
        )
