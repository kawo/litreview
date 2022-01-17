from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from litreview.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        ("Utilisateur", {"fields": ("name",)}),
    ) + auth_admin.UserAdmin.fieldsets  # type: ignore
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
