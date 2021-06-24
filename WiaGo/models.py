from django.db import models

# Create your models here.

class Node_R(models.Model):
    node_name = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=12, unique=True)
    longitude = models.DecimalField(max_digits=20,decimal_places=10)
    latitude = models.DecimalField(max_digits=20,decimal_places=10)
    date_creation = models.DateTimeField(auto_now_add=True)


class State(models.Model):
    ip_address = models.CharField(max_length=12)
    date_on = models.DateTimeField(auto_now_add=True)


class Notif(models.Model):
    name = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=12)
    type = models.CharField(max_length=12)
    date_on = models.DateTimeField(auto_now_add=True)