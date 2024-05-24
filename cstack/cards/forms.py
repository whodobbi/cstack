from django import forms
from django.core.exceptions import ValidationError

from cards.models import Card


class AddCardToCollectionForm(forms.Form):
    card = forms.ModelChoiceField(queryset=Card.objects.all())

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def clean_card(self):
        card = self.cleaned_data.get("card")
        if self.user.collection.filter(id=card.id).exists():
            raise ValidationError("you already have this card in your collection")
        return card
