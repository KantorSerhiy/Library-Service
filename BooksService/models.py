from django.db import models


class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "HARD"
        SOFT = "SOFT"

    title = models.CharField(max_length=53)
    author = models.CharField(max_length=53)
    cover = models.CharField(max_length=4, choices=CoverChoices.choices)
    inventory = models.PositiveSmallIntegerField()
    daily_fee = models.DecimalField("Daily fee in USD", max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.title} - {self.author} ({self.inventory})"
