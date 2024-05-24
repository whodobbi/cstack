from django.contrib.auth.models import AbstractUser
from django.db import models

from cards.models import Card # noqa
from myauth.validators import validate_image_size


class CstackUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    collection = models.ManyToManyField(
        "cards.Card",
        blank=True,
        related_name="users",
    )


class Profile(models.Model):
    objects = models.Manager()
    user: "CstackUser" = models.OneToOneField(
        CstackUser,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    image = models.ImageField(
        upload_to="media/user_images/",
        blank=True,
        null=True,
        validators=[validate_image_size],
    )
    username = models.CharField(max_length=60, default='user')
    birth_date = models.DateField("birth date", blank=True, null=True)
    country = models.CharField("country", max_length=50, blank=True)
    about = models.TextField(max_length=300, blank=True)
    bias = models.CharField(max_length=60, blank=True)
    entry_era = models.CharField("entry era", max_length=60, blank=True)
    fav_cards = models.TextField(blank=True)
    exp_card = models.CharField("the most expensive card", max_length=60, blank=True)
    des_card = models.CharField("the most desirable card", max_length=60, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"
