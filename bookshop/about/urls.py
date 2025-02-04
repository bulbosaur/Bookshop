import django.urls

import about.views

urlpatterns = [
    django.urls.path("", about.views.AboutSite.as_view(), name="about_site")
]