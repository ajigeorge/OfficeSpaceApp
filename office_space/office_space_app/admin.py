from django.contrib import admin

# Register your models here.
from .models import User, Building, Location, Floor, Seat

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','employee_name', 'email_id','user_role']

admin.site.register(User,UserAdmin)
admin.site.register(Building)
admin.site.register(Location)
admin.site.register(Floor)
admin.site.register(Seat)
