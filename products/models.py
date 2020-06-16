from django.db import models
# from django.db import connections
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='/default.jpeg', upload_to='profile_pics')
    username = models.CharField(max_length=200, null=True)
    pet = models.CharField(max_length=20, null=True)
    pet_image = models.ImageField(default="/default_pet.png", upload_to='profile_pics')
    pet_name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, null=True)
    breed = models.CharField(max_length=20, null=True)
    pet_birthday = models.DateField(max_length=20, null=True)
    pet_color = models.CharField(max_length=20, null=True)
    notes = models.TextField(null=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.user.name} Profile'


class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
