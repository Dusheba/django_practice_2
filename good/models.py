from django.db import models


class Good(models.Model):
    name = models.CharField(
        max_length=100
    )
    image = models.ImageField(
        upload_to="images/"
        verbose_name="Картинка"
    )
    price = models.IntegerField(
        null=True,
        blank=True
    )
