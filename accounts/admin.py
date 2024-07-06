from django.contrib import admin
from accounts.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'address', 'user']
    # list_filter = ['user']
