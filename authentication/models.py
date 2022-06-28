from ast import mod
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from requests import request
# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    num = models.CharField(max_length=10)
    appointment = models.CharField(max_length=250)
    dis = models.TextField()
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
