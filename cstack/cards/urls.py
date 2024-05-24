from django.urls import path

from cards import views

app_name = "cards"

urlpatterns = [
    path("list/", views.CardsList.as_view(), name="list"),
    path("<int:pk>/", views.CardDetail.as_view(), name="card_detail"),
    path("create/", views.CardCreate.as_view(), name="create_card"),
    path(
        "<int:card_id>/add_card/",
        views.AddCardView.as_view(),
        name="confirm_add_card",
    ),
]
