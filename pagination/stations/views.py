from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv

with open(BUS_STATION_CSV, "r", encoding="UTF-8") as file:
    reader = csv.DictReader(file)
    STATIONS = list(reader)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page"))
    if not page_number:
        page_number = 1
    paginator = Paginator(STATIONS, 15)
    paged_stations = paginator.get_page(page_number)
    context = {
        'bus_stations': paged_stations,
        'page': paged_stations
    }
    return render(request, 'stations/index.html', context)
