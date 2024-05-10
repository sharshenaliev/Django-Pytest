from django.contrib.auth.models import BaseUserManager


class EmailUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self.db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)
