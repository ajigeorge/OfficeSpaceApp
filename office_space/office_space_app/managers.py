from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email_id, password,):
        if not email_id:
            raise ValueError("Users must provide an email ID")
        email_id = self.normalize_email(email_id)
        user = self.model(email_id=email_id)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email_id, password,):
        user = self.create_user(email_id=self.normalize_email(email_id), password=password,)

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user