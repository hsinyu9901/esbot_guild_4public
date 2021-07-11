from django.shortcuts import render
from esapp.models import *

# 讀取資料表資料

## 旅行路線列表 + 旅行景點列表


def list_tripline(request):
    triplines = trip_line.objects.all()
    tripspots = trip_spot.objects.all()
    return render(request, "../templates/trip.html", locals())
