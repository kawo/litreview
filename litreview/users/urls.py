from django.urls import path
from litreview.users.views import user_detail_view, user_follow_view, user_redirect_view

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("<str:username>/follow/", view=user_follow_view, name="follow"),
]
