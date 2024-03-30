from django.db import models

# overriding/customizing default django model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager
# to retrieve settings from /profiles_project/settings.py
from django.conf import settings


# create model manager
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create and save a new user profile"""
        if not email:
            # raise an error
            raise ValueError('User must have an email address')
        # case-sensitive
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # hashed password
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new super user with given detail"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# extends AbstractBaseUser & PermissionsMixin
class UserProfile(AbstractBaseUser, PermissionsMixin):
    # readability
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # if a user's profile is activated or not
    is_active = models.BooleanField(default=True)
    # if a user is a staff user
    is_staff = models.BooleanField(default=False)

    # model manager for django
    objects = UserProfileManager()

    # for django admin and auth system
    # override
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # functions
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    # string representation
    def __str__(self):
        """Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    # use foreign key to connect model to model
    user_profile = models.ForeignKey(
        # to replace the UserProfile
        settings.AUTH_USER_MODEL,
        # if user is deleted, all the feeds are deleted too
        on_delete=models.CASCADE
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text