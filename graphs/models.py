from django.db import models

# Create your models here.
class Stock(models.Model):
    # define db 
    ticker = models.CharField(max_length=10)  # data type

    # 
    def __str__(self):
        return self.ticker

