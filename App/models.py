from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile = models.ImageField(upload_to='profile_images', default='book-icon.png')
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
