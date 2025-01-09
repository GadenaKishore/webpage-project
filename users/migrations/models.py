from django.db import models

# Create your models here.

class registrationmodel(models.Model):
    name = models.CharField(max_length = 20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length = 20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

