from django.db import models

from django.contrib.auth.models import  User

class Profile(models.Model):
    # Cascade ===> User deleted in db == delete also profile
    # but deleting the profile won't delete the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    # to be more descriptive when dealing with the profile
    def __str__(self):
        return f'{self.user.username} Profile'

