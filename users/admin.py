from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Level

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'phone_number', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Contact info', {'fields': ('phone_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'points')
    raw_id_fields = ('user',)

admin.site.register(Profile, ProfileAdmin)

class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'description')
    ordering = ('order',)

admin.site.register(Level, LevelAdmin)