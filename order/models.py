from django.db import models
from good.models import Good


class Order(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    id_goods = models.ForeignKey(Good, on_delete=models.CASCADE)


def __str__(self):
    return "{} {}".format(self.name, self.date_created, self.id_goods)
