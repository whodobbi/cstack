from django.contrib.auth.views import LogoutView
from django.urls import path

from myauth.views import (
    CustomLoginView,
    MyUserCreateView,
    ProfileView,
    EditProfileView,
)

app_name = "myauth"

urlpatterns = [
    path("register/", MyUserCreateView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", EditProfileView.as_view(), name="edit_profile"),
]
