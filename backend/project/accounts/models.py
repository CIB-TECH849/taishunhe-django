from django.db import models
from django.contrib.auth.models import User

# Extend user profile if needed
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, default='normal')
