from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
<<<<<<< HEAD
    def create_user(self, email_id, employee_name, password,**other_fields):
        if not email_id:
            raise ValueError("Users must provide an email ID")
        email_id = self.normalize_email(email_id)
        user = self.model(email_id=email_id, employee_name=employee_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email_id, employee_name, password, **other_fields):
        # user = self.create_user(email_id=self.normalize_email(email_id), password=password,)
        # user.is_staff = True
        # user.is_superuser = True
        # user.is_active = True
        # user.save()
        # return user
=======
    def create_user(self, email_id,employee_name, password,**other_fields):
        if not email_id:
            raise ValueError("Users must provide an email ID")
        email_id = self.normalize_email(email_id)
        user = self.model(email_id=email_id, employee_name=employee_name,
                           **other_fields)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email_id, employee_name, password, **other_fields):

>>>>>>> 1776602e726e7a7edd9ec0805cd132df8c8376b7
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
<<<<<<< HEAD
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
=======
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
>>>>>>> 1776602e726e7a7edd9ec0805cd132df8c8376b7

        return self.create_user(email_id, employee_name, password, **other_fields)