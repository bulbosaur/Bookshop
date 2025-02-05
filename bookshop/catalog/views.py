import django.http
import django.shortcuts
import django.views

import catalog.models


class ItemList(django.views.View):
    def get(self, request, *args, **kwargs):
        catalog_book = catalog.models.Book.objects.all()
        return django.shortcuts.render(
            request,
            "book_list.html",
            context={"catalog_book": catalog_book},
        )


class Item(django.views.View):
    def get(self, request, item_id, *args, **kwargs):
        book = django.shortcuts.get_object_or_404(catalog.models.Book, id=item_id)
        return django.shortcuts.render(
            request,
            "book_page.html",
            context={"title": book.title, "description": book.description, "main_img": book.main_photo},
        )
