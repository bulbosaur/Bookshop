import django.conf
import django.urls

import catalog.views

from django.conf.urls.static import static

urlpatterns = [
    django.urls.path("", catalog.views.ItemList.as_view(), name="item_list"),
    django.urls.path("<int:item_id>/", catalog.views.Item.as_view(), name="item"),
]

if django.conf.settings.DEBUG:
    urlpatterns += static(django.conf.settings.MEDIA_URL, document_root=django.conf.settings.MEDIA_ROOT)