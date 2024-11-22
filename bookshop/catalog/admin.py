import django.contrib
import django.contrib.admin
import catalog.models

class ItemAdmin(django.contrib.admin.ModelAdmin):
    list_display = [
        catalog.models.Book.id.field.name,
        catalog.models.Book.title.field.name,
    ]