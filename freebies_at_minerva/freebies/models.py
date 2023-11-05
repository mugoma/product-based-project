from django.db import models

# Create your models here.


CITIES = [
    ('BERLIN', 'Berlin'),
    ('BUENOS_AIRES', 'Buenos Aires'),
    ('HYDERABAD', 'Hyderabad'),
    ('LONDON', 'London'),
    ('SAN_FRANCISCO', 'San Francisco'),
    ('SEOUL', 'Seoul'),
    ('TAIPEI', 'Taipei')
]


class Freebie(models.Model):
    title = models.TextField()
    description = models.TextField()
    percentage_off = models.DecimalField(max_digits=3, decimal_places=1)
    amount_off = models.DecimalField(max_digits=5, decimal_places=1)

    city = models.TextField(choices=CITIES)

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.PositiveBigIntegerField(default=0)

