from django.db import models
from freebies.models import CITIES

# Create your models here.


class CityNotifications(models.Model):
    city = models.TextField(choices=CITIES)
    user = models.ForeignKey('authentication.user',
                             models.CASCADE, null=True, blank=True)
