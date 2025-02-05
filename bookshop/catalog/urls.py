import django.urls

import catalog.views

urlpatterns = [
    django.urls.path("", catalog.views.ItemList.as_view(), name="item_list"),
    django.urls.path("<int:item_id>/", catalog.views.Item.as_view(), name="item"),
]
