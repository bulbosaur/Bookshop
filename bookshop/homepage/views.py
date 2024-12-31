import django.http
import django.views
import django.shortcuts

import catalog.models

class Home(django.views.View):
    def get(self, request, *args, **kwaigs):
        book_one = django.shortcuts.get_object_or_404(catalog.models.Book, id=1)
        return django.shortcuts.render(
            request,
            "index.html",
            context={"title_one": book_one.title, "price_one": book_one.price}
        )
