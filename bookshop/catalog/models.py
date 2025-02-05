import django.db.models


def get_upload_path(instance, filename):
    return f"books/{instance.id}/{filename}"


class Book(django.db.models.Model):
    title = django.db.models.CharField("Название", max_length=250)
    author = django.db.models.CharField("Автор", max_length=250)
    description = django.db.models.TextField("Описание")
    price = django.db.models.FloatField("Цена", default=500)
    publication_date = django.db.models.DateField()
    main_photo = django.db.models.ImageField(
        "Главное фото", blank=True, upload_to=get_upload_path
    )


class Meta:
    verbose_name = "Товар"
    verbose_name_plural = "Товары"


def __str__(self):
    return self.name
