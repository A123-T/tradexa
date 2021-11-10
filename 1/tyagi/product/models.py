from django.db import models
import datetime
# Create your models here.
class producti(models.Model):
    name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())

