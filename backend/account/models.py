from django.db import models

from django.contrib.auth.models import AbstractUser # override default user model 'from django.contrib.auth.models import User'

# Custom user model
# https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#specifying-a-custom-user-model

class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name'] # will prompt these when do createsuperuser

    def __init__(self, *args, **kwargs):
        self._meta.get_field('email').blank = False # alter the value in AbstractUser w/o additional settings: https://stackoverflow.com/questions/45722025/forcing-unique-email-address-during-registration-with-django
        self._meta.get_field('email')._unique = True
        self._meta.get_field('first_name').blank = False
        self._meta.get_field('last_name').blank = False
        super(CustomUser, self).__init__(*args, **kwargs)
    
    def __str__(self):
        return self.username