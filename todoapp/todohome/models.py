from django.db import models # type: ignore


class todomodel(models.Model):
    title           = models.CharField(max_length=255)
    description     = models.TextField(max_length=600)
    datecomplete    = models.CharField(max_length=30)
    status          = models.BooleanField(default=False)
    soft_del        = models.BooleanField(default=False)
