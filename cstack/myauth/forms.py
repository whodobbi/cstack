from django.contrib.auth.forms import UserCreationForm
from django import forms

from myauth.models import CstackUser, Profile


class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = CstackUser
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ""

    def save(self, commit=True):
        super().save(commit=commit)
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "image", "username", "birth_date", "country", "about", "bias",
            "entry_era", "fav_cards", "exp_card", "des_card"
        ]
