from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display =["pkid", "id", "email", "username", "first_name", "last_name", "is_staff", "is_active"]
    list_display_links = ["id", "email"]
    fieldsets = (
        (
            _("Login Credentials"), {
                "fields" : ("email", "password",)
            },
        ),
        (
            _("Personal Inforfmation"),
            {
                "fields":("username", "first_name", "last_name")
            },
        ),
        (
            _("Permissons and Groups"), {
                "fields":("is_active", "is_staff", "is_superuser", "groups", "user_permission",)
            }
        ),
        (
            _("Important Dates"), {
                "fields": ("last_login", "date_joined")

            }
        ),
    )
    add_fieldsets=(
            (None, {
                "classes":("wide", ), 
                "fields":("email", "password1", "password2", "is_staff", "is_active")            })
        )
    
    search_fields = ["email", "first_name", "last_name "]




admin.site.register(User,UserAdmin)
    