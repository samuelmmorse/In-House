from django.db import models

# Create your models here.
class Reservation(models.Model):
    topic = models.TextField()
    duration = models.TextField(default="15 Minutes")
    student = models.TextField()
    helper = models.TextField()
    feedback = models.TextField(default="")
