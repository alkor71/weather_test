# from django.shortcuts import render
#
# # Create your views here.
import requests
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from .models import City
from django.views import View

key = settings.WEATHER_API_KEY


class CityAutocomplete(View):
    def get(self, request):
        q = request.GET.get('term', '')
        if q:
            cities = City.objects.filter(name__istartswith=q).order_by('name')[:10]
            results = list(cities.values_list('name', flat=True))
        else:
            results = []
        return JsonResponse(results, safe=False)


def find_city(city_name):
    try:
        res = requests.get("http://api.openweathermap.org/geo/1.0/direct",
                           params={'q': city_name, 'limit': 3, 'appid': key})
        data = res.json()
        city_lat, city_lon = round(data[0]['lat'], 2), round(data[0]['lon'], 2)
        # print(city_lat, city_lon)
        return city_lat, city_lon

    except Exception as e:
        print("Exception (find):", e)
        pass


def check_weather(request):
    city = None
    weather = None
    temp = None
    wind = None
    if request.method == 'POST' and 'city' in request.POST:
        city_name = request.POST['city']
        try:
            city_lat, city_lon = find_city(city_name)
            print(city_lat, city_lon)
            res = requests.get(
                f'https://api.openweathermap.org/data/2.5/forecast?lat={city_lat}&lon={city_lon}&units=metric&cnt=1&lang=ru&appid={key}')

            if res.status_code == 200:
                print('success')
                city = res.json()['city']['name']
                weather = res.json()['list'][0]['weather'][0]['description']
                temp = res.json()['list'][0]['main']['temp']
                wind = res.json()['list'][0]['wind']['speed']
            else:
                print('fail')

        except Exception as e:
            city = {'error': 'Город не найден'}

    return render(request, 'main\index.html', {'city': city, 'weather': weather, 'temp': temp, 'wind': wind})
