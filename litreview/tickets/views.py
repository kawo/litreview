from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Ticket


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
