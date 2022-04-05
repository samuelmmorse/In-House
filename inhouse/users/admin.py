from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .models import Topic

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_student",
        "is_helper",
        "is_admin",
        "picture",
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "picture")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        (
            "Additional info",
            {"fields": ("is_student", "is_helper", "is_admin", "classStanding", "position", "topics", "personalBio")},
        ),
    )

    add_fieldsets = (
        (None, {"fields": ("username", "password1", "password2")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        (
            "Additional info",
            {"fields": ("is_student", "is_helper", "is_admin", "classStanding", "position", "topics", "personalBio")},
        ),
    )


admin.site.register(User, CustomUserAdmin)
