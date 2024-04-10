from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )
    
class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Enter name for tag")
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class Image(models.Model):
    """Model representing a Image"""
    name= models.CharField(
        max_length=100,
        unique=True,
        help_text="Enter a name for the image."
    )
    
    time_date= models.DateTimeField(auto_now=False, auto_now_add=False)

    description= models.CharField(
        max_length=250,
        help_text="Enter image description."
    )
    tags= models.ManyToManyField(Tags, help_text="Choose tags for image")

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Album(models.Model):
    name= models.CharField(
        max_length=100,
        unique=True,
    )

    patterns = (
        ('r', 'Random'),
        ('c', 'Chronological'),
    )

    display_pattern= models.CharField(
        max_length=1,
        choices=patterns,
        blank=True,
        default='r',
        help_text="Display patterns",
    )

    tags= models.ManyToManyField(Tags, help_text="select tags for image")

#many to many to tags 

    def __str__(self):
        """String for representing the Model object."""
        return self.name