import django.contrib.auth.views
import django.urls

import account.views

urlpatterns = [
    django.urls.path(
        "login/",
        django.contrib.auth.views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),
    django.urls.path(
        "logout/",
        django.contrib.auth.views.LogoutView.as_view(
            template_name="registration/login.html"
        ),
        name="logout",
    ),
    django.urls.path("signup/", account.views.SignUp.as_view(), name="signup"),
    django.urls.path(
        "user_profile/<int:pk>/",
        account.views.ShowProfilePage.as_view(),
        name="user_profile",
    ),
]
