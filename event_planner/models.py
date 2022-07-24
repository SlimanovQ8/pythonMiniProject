from django.db import models

# Create your models here.
class Event(models.Model):
    organizer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    image = models.TextField(max_length=1000)
    num_of_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name}: {self.image}"