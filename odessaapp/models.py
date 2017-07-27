from django.db import models

class DailyDish(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nazwa dania", blank=False, null=False)
    description = models.TextField(verbose_name="Opis dania")

    def __str__(self):
        return self.name
class CurrentDailyDish(models.Model):
    current_dish = models.ForeignKey(DailyDish)

    def __str__(self):
        return "Obecne danie dnia: {}".format(self.current_dish.name)

class Musician(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    photo_link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

