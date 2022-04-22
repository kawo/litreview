from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .models import Ticket


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ["title", "description", "image"]


ticket_add_view = TicketCreateView.as_view()
