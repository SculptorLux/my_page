from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def get_info_about_sign_zodiac(request, sign_zodiac):
    if sign_zodiac == 'scorpio':
        return HttpResponse("Знак зодиака - скорпион")
    elif sign_zodiac == 'leo':
        return HttpResponse("Знак зодиака - лев")
    else:
        return HttpResponseNotFound("Не найдена такая страница")