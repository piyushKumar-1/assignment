from django.db import models
from django.contrib.auth.models import User


class Advisor(models.Model):
    name = models.CharField(max_length=200)
    profile_pic = models.URLField(max_length=1000)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
