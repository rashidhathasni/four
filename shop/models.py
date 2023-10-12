from django.db import models

class Producct(models.Model):
    item=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.CharField(max_length=500)
    def __str__(self):
        return self.item