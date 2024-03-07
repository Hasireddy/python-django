from django.db import models

class Register(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.TextField()
    confirmPassword = models.TextField()