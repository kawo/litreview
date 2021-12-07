from django.urls import path
from litreview.users.views import user_index_view

app_name = "users"
urlpatterns = [
    path(route="<str:username>/", view=user_index_view, name="index"),
]
