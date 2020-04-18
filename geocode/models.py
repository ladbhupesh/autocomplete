from django.db import models

class Coordinate(models.Model):
    code = models.CharField(max_length=150)
    def __str__(self):
        return self.code

class Profiles(models.Model):
    geocode=models.CharField(max_length=200)
    country=models.CharField(max_length=500)
    city=models.CharField(max_length=500)

    class Meta:
        managed=False
        db_table='profiles_country'

    def __str__(self):
        return '{}'.format(self.geocode)
# Create your models here.
