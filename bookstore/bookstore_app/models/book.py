from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField()


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=4)
    publication_date = models.DateField(null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)






