from django.db import models

# Create your models here.
class Locations(models.Model):
    name = models.CharField(max_length=40)
    path = models.CharField(max_length=300)

    def __str__(self):
        return self.name