from django.db import models


class CardCategory(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Card(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        CardCategory,
        on_delete=models.CASCADE,
        related_name="cards",
    )
    release_year = models.IntegerField()
    release_country = models.CharField(max_length=30, blank=False)
    album = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    shop = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="card_images/", blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"
