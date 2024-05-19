from django.contrib import admin
from .models import CustomUser, UserProfile
# from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# User = get_user_model()
# admin.site.unregister(User)


class UserProfileInLine(admin.StackedInline):
    model = UserProfile


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    inlines = [UserProfileInLine]


admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(CustomUser)
