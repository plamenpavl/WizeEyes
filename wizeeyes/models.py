from django.db import models

class Glasses(models.Model) :
    title = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.title} priced at £{self.price}'