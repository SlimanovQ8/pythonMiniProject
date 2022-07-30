import datetime

from django.db import models
from django.core.exceptions import ValidationError
import re
from django import forms
from django.utils.safestring import mark_safe

# Create your models here.
def NameValidation(value):
    if "event" in value:
        raise ValidationError("Word \"event\" should not be included on event name field")
    else:
        return value

def EmailValidation(value):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, value):
        return value
    raise ValidationError("email is not valid")

def SeatsMinimumNumberValidation(value):
    if value > 4:
        return value
    raise ValidationError("number of seats can't be less than 5")

def isDateAfterToday(value):
    if value > datetime.date.today():
        return value
    raise ValidationError("The start date of the event must be after today's date")

def BookedSeatsValidation(booked_seats, num_of_seats):
    if booked_seats > num_of_seats:
       return "Booked seats are more than the available seats"
    return ""

def DatesValidation(start_date, end_date):
    if end_date < start_date:
       return "The event end date is before event start date"
    return ""
class Event(models.Model):

    organizer = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, validators=[NameValidation])
    email = models.CharField(max_length=254, validators= [EmailValidation])
    image = models.TextField(max_length=1000)
    num_of_seats = models.PositiveIntegerField(
        validators=[SeatsMinimumNumberValidation])
    booked_seats = models.PositiveIntegerField(
        default=0,

        )

    start_date = models.DateField(validators= [isDateAfterToday])
    end_date = models.DateField()

    def clean(self):
        bookedSeatsValidation = BookedSeatsValidation(booked_seats=self.booked_seats, num_of_seats=self.num_of_seats)
        dateValidation = DatesValidation(start_date=self.start_date, end_date=self.end_date)

        if not bookedSeatsValidation == "" or not dateValidation == "":
            raise ValidationError(mark_safe(f"{bookedSeatsValidation} <br/> {dateValidation}"))

    def __str__(self):
        return f"{self.name}: {self.image}"