from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    FormView,
)

from cards.forms import (
    AddCardToCollectionForm,
)
from cards.models import Card, CardCategory


class CardsList(
    LoginRequiredMixin,
    ListView,
):
    page_title = "Cards"
    model = Card
    context_object_name = "cards"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CardCategory.objects.all()
        return context


class CardDetail(
    LoginRequiredMixin,
    DetailView,
):
    model = Card


class CardCreate(
    PermissionRequiredMixin,
    CreateView,
):
    model = Card
    fields = "__all__"
    success_url = "/"
    permission_required = "cards.add_card"


class AddCardView(LoginRequiredMixin, FormView):
    form_class = AddCardToCollectionForm
    template_name = "cards/confirm_add_card.html"
    success_url = reverse_lazy("profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card_id = self.kwargs.get("card_id")
        context["card"] = Card.objects.get(id=card_id)
        return context

    def form_valid(self, form):
        card = form.cleaned_data["card"]
        self.request.user.collection.add(card)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
