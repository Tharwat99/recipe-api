from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        """ create and save data for new user """
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using= self._db)
        return user
