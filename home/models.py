import random
from django.db import models

# Create your models here.
class Quiz(models.Model):
    num1 = models.BigIntegerField()
    num2 = models.BigIntegerField()
    def sum(self):
        return self.num1 + self.num2
