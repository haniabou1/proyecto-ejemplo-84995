from django.urls import path, include
from .views import (
    signup_view,
    profile_view,
    profile_edit_view,
    CustomPasswordChangeView,
)

urlpatterns = [

    path("signup/", signup_view, name="signup"),

    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),

    path(
        "password_change/",
        CustomPasswordChangeView.as_view(),
        name="password_change",
    ),

    path("", include("django.contrib.auth.urls")),
]
