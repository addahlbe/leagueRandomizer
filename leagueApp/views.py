from django.shortcuts import render
from models import Hero


def home(request):
    all_heros = Hero.objects.all()
    mid = Hero.objects.filter(primary_role="Mid")
    top = Hero.objects.filter(primary_role="Top")
    adc = Hero.objects.filter(primary_role="ADC")
    support = Hero.objects.filter(primary_role="Support")
    jungle = Hero.objects.filter(primary_role="Jungle")
    return render(request, 'home.html', {
        'all_heros': all_heros,
        'mid': mid,
        'top': top,
        'adc': adc,
        'support': support,
        'jungle': jungle})


def signup(request):
    return render(request, 'signup.html',)
