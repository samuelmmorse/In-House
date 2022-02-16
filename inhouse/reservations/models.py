from django.db import models

# Create your models here.
class Reservation(models.Model):
    course = models.TextField()
    topic = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    student = models.TextField()
    helper = models.TextField()
    feedback = models.TextField()
