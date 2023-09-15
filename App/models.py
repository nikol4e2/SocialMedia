from django.db import models

# Create your models here.

class Profile (models.Model):
    user = pass
    id_user = pass
    bio = pass
    profile = models.ImageField(upload_to='profile_images',default='book-icon.png')
    location = pass

