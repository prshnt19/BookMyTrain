from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Register(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.IntegerField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    varify_password = models.CharField(max_length=15)


class Train(models.Model):
    train_no = models.IntegerField(primary_key=True)
    train_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)

    def __unicode__(self):
        return (str(self.train_no) + '\t' + self.train_name)

    def __str__(self):
        return (str(self.train_no) + '\t' + self.train_name)


class Station(models.Model):
    station_name = models.CharField(max_length=30)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    arrival_time = models.CharField(max_length=30)
    departure_time = models.CharField(max_length=30)
    platform = models.IntegerField()

    def __unicode__(self):
        return self.station_name

    def __str__(self):
        return self.station_name



class Ticket(models.Model):
    pnr = models.IntegerField(primary_key=True)
    train_no = models.ForeignKey(Train, on_delete=models.CASCADE)
    train_name = models.CharField(max_length=30)
    coach_no = models.CharField(max_length=10)
    seat_no = models.IntegerField()
    from_station = models.CharField(max_length=30)
    to_station = models.CharField(max_length=30)
    fair = models.IntegerField()
    d_o_j = models.DateField()

class Passenger(models.Model):
    name = models.CharField(max_length=30)
    pnr =  models.ForeignKey(Ticket, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.ForeignKey(Register, on_delete=models.CASCADE)
