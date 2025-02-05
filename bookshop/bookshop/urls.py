import django.contrib
import django.urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    django.urls.path("admin/", django.contrib.admin.site.urls),
    django.urls.path("", django.urls.include("homepage.urls")),
    django.urls.path("catalog/", django.urls.include("catalog.urls")),
    django.urls.path("about/", django.urls.include("about.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
