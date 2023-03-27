from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    authenticated = models.BooleanField(default=False)
    image_field = models.ImageField(upload_to="/media/", default=None)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username} Account"

