from django.urls import path

from . import views

app_name = "tickets"
urlpatterns = [
    path(route="", view=views.TicketListView.as_view(), name="list"),
]
