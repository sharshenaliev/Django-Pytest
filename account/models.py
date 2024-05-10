from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from account.auth import EmailUserManager


class MyUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    favorite = models.ManyToManyField("book.Book", verbose_name='Избранные книги')

    USERNAME_FIELD = 'email'

    objects = EmailUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
