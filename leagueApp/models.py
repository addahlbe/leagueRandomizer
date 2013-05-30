from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=20)
    primary_role = models.CharField(max_length=10)
    secondary_role = models.CharField(max_length=10)
    passive = models.CharField(max_length=30)
    spell1 = models.CharField(max_length=100)
    spell2 = models.CharField(max_length=100)
    spell3 = models.CharField(max_length=100)
    spell4 = models.CharField(max_length=100)


class User(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
