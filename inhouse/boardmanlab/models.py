from os import major
from django.db import models
from users import models as u
# Create your models here.

class helpSession(models.Model):
    helper = models.ForeignKey(u.User, on_delete=models.CASCADE)
    topic = models.TextField(max_length=300)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    duration = models.IntegerField(default=30)
    attendance = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ["time"]


class myAccount(models.Model):
    userYear = models.TextChoices
    classesTaking = models.TextChoices
    userPosition = models.TextChoices
    userProficiencies = models.TextChoices
    userBio = models.TextField(max_length=1000)



