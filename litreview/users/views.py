from itertools import chain

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import CharField, Value
from django.urls import reverse
from django.views.generic import DetailView, RedirectView
from litreview.reviews.models import Review
from litreview.tickets.models import Ticket

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews = Review.objects.all().filter(user=self.request.user)
        # returns queryset of reviews
        reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

        tickets = Ticket.objects.all().filter(user=self.request.user)
        # returns queryset of tickets
        tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

        # combine and sort the two types of posts
        posts = sorted(
            chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
        )

        context["posts"] = posts
        return context


user_detail_view = UserDetailView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},  # type: ignore
        )


user_redirect_view = UserRedirectView.as_view()


class UserFollowView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_follow_view = UserFollowView.as_view()
