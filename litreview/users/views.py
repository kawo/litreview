from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

User = get_user_model()


class UsersIndexView(LoginRequiredMixin, View):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_index_view = UsersIndexView.as_view()
