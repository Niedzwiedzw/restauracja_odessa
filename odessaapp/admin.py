from django.contrib import admin
from odessaapp.models import DailyDish, CurrentDailyDish, Musician
# Register your models here.

admin.site.register(DailyDish)
admin.site.register(CurrentDailyDish)
admin.site.register(Musician)
