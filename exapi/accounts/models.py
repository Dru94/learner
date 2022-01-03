from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.text import slugify
# Create your models here.

LEVEL_CHOICES = [
    ('primary', 'primary'),
    ('secondary', 'secondary')
]


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')

        if email is None:
            raise TypeError('Users should have an Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        if email is None:
            raise TypeError('Users should have an Email')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=225, unique=True, db_index=True)
    first_name = models.CharField(max_length=225, blank=True)
    last_name = models.CharField(max_length=225, blank=True)
    email = models.EmailField(max_length=225, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    level = models.CharField(
        max_length=9, choices=LEVEL_CHOICES, blank=False, default='')
    level_number = models.PositiveIntegerField(
        null=False, default=1, verbose_name='class')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True, default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email + ' Class: ' + str(self.level) + str(self.level_number)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.first_name)

        return super().save(*args, **kwargs)
