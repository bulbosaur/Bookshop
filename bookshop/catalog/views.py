import django.http
import django.shortcuts
import django.views

import catalog.models


class ItemList(django.views.View):
    template_name = "books.html"

    def get(self, request, *args, **kwaigs):
        return django.http.HttpResponse("Books")
        # return django.shortcuts.render("book_list.html")


class Item(django.views.View):
    def get(self, request, item_id, *args, **kwaigs):
        book = django.shortcuts.get_object_or_404(catalog.models.Book, id=item_id)
        return django.shortcuts.render(
            request,
            "book_page.html",
            context={"title": book.title, "description": book.description}
        )
