import django.http
import django.views

import catalog.models

class ItemList(django.views.View):
    template_name = "books.html"
    def get(self, request, *args, **kwaigs):
        model = catalog.models.Book
        return django.http.HttpResponse('Book')
    
class Item(django.views.View):
    def get(self, request, item_id, *args, **kwaigs):
        return django.http.HttpResponse(f'{item_id}')