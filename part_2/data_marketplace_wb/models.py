from django.db import models

# Create your models here.


class data_wb_card(models.Model):
    article = models.IntegerField()
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
