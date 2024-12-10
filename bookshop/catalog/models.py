import django.db.models


class Book(django.db.models.Model):
    title = django.db.models.CharField("Название", max_length=250)
    author = django.db.models.CharField("Автор", max_length=250)
    description = django.db.models.TextField("Описание")
    price = django.db.models.FloatField("Цена", default=500)
    publication_date = django.db.models.DateField()


class Meta:
    verbose_name = "Товар"
    verbose_name_plural = "Товары"


def __str__(self):
    return self.name
