from django.db import models

# Create your models here.


class Assistance(models.Model):
    name = models.CharField(max_length=20)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    description = models.CharField(max_length=200,blank=True,null=True)
    type = models.CharField(max_length=50,choices=(('Petrol Bunk', 'Petrol Bunk'),
                                           ('Mechanic', 'Mechanic')))

    def __str__(self):
        return self.name
    