from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 120)
    code = models.CharField(max_length = 10, unique = True)
    categ = models.IntegerField()

    def __str__(self):
        return self.name