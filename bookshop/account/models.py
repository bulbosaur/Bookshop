import django.contrib.auth
import django.dispatch
import django.db.models


class Profile(django.db.models.Model):
    user = django.db.models.OneToOneField(
        django.contrib.auth.models.User, null=True, on_delete=django.db.models.CASCADE
    )
    bio = django.db.models.TextField(null=True, blank=True)
    profile_pic = django.db.models.ImageField(
        null=True, blank=True, upload_to="images/profile/"
    )
    facebook = django.db.models.CharField(max_length=50, null=True, blank=True)
    twitter = django.db.models.CharField(max_length=50, null=True, blank=True)
    instagram = django.db.models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = "account"

    def __str__(self):
        return str(self.user)


@django.dispatch.receiver(
    django.db.models.signals.post_save, sender=django.contrib.auth.models.User
)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
