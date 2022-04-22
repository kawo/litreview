from django.urls import path
from litreview.tickets.views import ticket_add_view

app_name = "tickets"
urlpatterns = [
    path("add/", view=ticket_add_view, name="add"),
]
