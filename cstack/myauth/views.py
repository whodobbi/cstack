from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView

from myauth.forms import MyUserCreateForm, ProfileEditForm
from myauth.models import CstackUser, Profile


class BaseView(TemplateView):
    template_name = "base.html"


class HomeView(TemplateView):
    template_name = "home.html"


class CustomLoginView(LoginView):
    success_url = reverse_lazy("home")


class MyUserCreateView(CreateView):
    model = CstackUser
    success_url = reverse_lazy("home")
    form_class = MyUserCreateForm

    def get_success_url(self):
        user = self.object
        login(self.request, user)
        return super().get_success_url()


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "myauth/profile.html"
    context_object_name = "profile"

    def get_object(self, **kwargs):
        return Profile.objects.get(user=self.request.user)


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = CstackUser
    form_class = ProfileEditForm
    template_name = "myauth/edit_profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user
