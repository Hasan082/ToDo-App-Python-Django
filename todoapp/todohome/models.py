from django.db import models

# Create your models here.
class todomodel(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)


def __str__(self)-> str:
    return f"{self.firstName} {self.lastName}"