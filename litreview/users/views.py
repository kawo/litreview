from django.http import HttpResponse
from django.views.generic import View


class UsersView(View):
    def index(request):
        return HttpResponse("Hello, world!")
