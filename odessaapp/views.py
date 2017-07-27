from django.shortcuts import render, redirect
from odessaapp.models import CurrentDailyDish, DailyDish
from odessaapp.forms import DailyDishForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def dish():
    return CurrentDailyDish.objects.first()


def current_dish():
    return DailyDish.objects.get(currentdailydish=CurrentDailyDish.objects.first())


def index(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def site_maintenence(request):
    return render(request, 'site_maintenence.html')


def daily_dish(request):
    dish = current_dish()
    dishchoices = DailyDish.objects.all()

    return render(request, 'daily_dish.html', {'dish': dish,
                                               'dishchoices': dishchoices, })


def change_dish(request, dish_id):
    obj = dish()

    obj.current_dish = DailyDish.objects.get(id=dish_id)
    obj.save()
    return redirect('daily_dish')


@login_required
def add_dish(request):
    if request.method == 'POST':
        form = DailyDishForm(request.POST)
    else:
        form = DailyDishForm()

    if form.is_valid():
        form.save()
        return redirect('daily_dish')

    return render(request, 'add_dish.html', {'form': form})





