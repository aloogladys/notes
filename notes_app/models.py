from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null= True, blank = True)

