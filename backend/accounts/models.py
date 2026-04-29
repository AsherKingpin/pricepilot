from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "admin"
        MANAGER = "MANAGER", "manager"
        USER = "USER", "user"
    role = models.CharField(
        max_length = 10,
        choices = Roles.choices,
        default=Roles.USER
    )
    #function to check if user is admin
    def is_admin(self):
        return self.role == self.Roles.ADMIN
    #function to check if user is manager
    def is_manager(self):
        return self.role == self.Roles.MANAGER
    # dunder function to save the object meaningfully
    def __str__(self):
        return f"{self.username} ({self.role})"