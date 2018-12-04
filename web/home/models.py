from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=40)
    path = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Order(models.Model):
    source = models.ForeignKey(Location, related_name ='source_loc', on_delete = models.CASCADE)
    destination = models.ForeignKey(Location, related_name = 'destination_loc', on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (str(self.source)+'-' +str(self.destination))