from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Ajoutez d'autres champs de profil au besoin

    def _str_(self):
        return self.user.username

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.FileField(blank= True, null= True, upload_to='products')
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added']

    def _str_(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name                                                                                                                                                                                                                                                                                                                                     
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def _str_(self):
        return self.title