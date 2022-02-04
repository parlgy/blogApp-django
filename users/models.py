from tkinter import Image
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
# CASCADE means if a user is deleted also delete the profile but if a profile is deleted then the user not will be deleted

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# Overriding the save method of a model
#resizing te profile image
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

