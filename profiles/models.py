from django.db import models

# Create your models here.

class Profiles(models.Model):
    image_field = models.ImageField(upload_to="/media/")
    createdat = models.DateTimeField(auto_now_add=True)

