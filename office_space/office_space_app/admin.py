from django.contrib import admin

# Register your models here.
from .models import User, Building, Location, Floor, Seat

admin.site.register(User,)
class UserAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'email_id','user_role']