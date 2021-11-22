from django.db import models
import re
# import bcrypt
# Create your models here.

class Location(models.Model):
    location_code = models.CharField(max_length=5)
    description = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city

class Building(models.Model):
    building_code = models.CharField(max_length=5)
    description = models.CharField(max_length=255)
    location_code = models.CharField(max_length=5)
    location = models.ForeignKey(Location, related_name="location_buildings", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.description

class Floor(models.Model):
    floor_code = models.CharField(max_length=5)
    building_code = models.CharField(max_length=5)
    description = models.CharField(max_length=255)
    location_code = models.CharField(max_length=5)
    location = models.ForeignKey(Location, related_name="location_floors", on_delete = models.CASCADE)
    building = models.ForeignKey(Building, related_name="building_floors", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Floor " + self.floor_code + " " + self.location.__str__() + " " + self.building.__str__()

class Seat(models.Model):
    seat_number = models.CharField(max_length=25)
    seat_type = models.CharField(max_length=45)
    floor_code = models.CharField(max_length=5)
    building_code = models.CharField(max_length=5)
    location_code = models.CharField(max_length=5)
    location = models.ForeignKey(Location, related_name='location_seats', on_delete = models.CASCADE)
    building = models.ForeignKey(Building, related_name='building_seats', on_delete = models.CASCADE)
    floor = models.ForeignKey(Floor, related_name='floor_seats', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.seat_number + self.seat_type + self.location + self.building + self.location


class User(models.Model):
    USER_ROLE = (
        ('Admin', 'Admin'),
        ('Location_anchor', 'Location_anchor'),
        ('Building_anchor', 'Building_anchor'),
        ('Floor_anchor', 'Floor_anchor'),
    )
    employee_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    location_code = models.CharField(max_length=5)
    building_code = models.CharField(max_length=5)
    floor_code = models.CharField(max_length=5)
    user_role = models.CharField(max_length=45, choices=USER_ROLE)
    location = models.ForeignKey(Location, related_name="location_users", on_delete = models.CASCADE,default = 1)
    building = models.ForeignKey(Building, related_name="building_users",on_delete = models.CASCADE, default = 1)
    floor = models.ForeignKey(Floor, related_name="floor_users",on_delete = models.CASCADE, default = 1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.employee_name



