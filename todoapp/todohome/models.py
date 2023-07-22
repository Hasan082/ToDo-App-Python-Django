from django.db import models


class todomodel(models.Model):
    title           = models.CharField(max_length=255)
    description     = models.TextField(max_length=1000)
    datecomplete    = models.DateField()