from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=128)
    price = models.IntegerField()

    def __str__(self):
        return self.name