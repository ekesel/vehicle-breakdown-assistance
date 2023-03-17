from django.shortcuts import render
from .models import Assistance
from math import radians, sin, cos, sqrt, atan2


def get_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # Apply the Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c
    return distance

def index(request):
    nearby_petrol_bunks = []
    nearby_mechanics = []
    if request.POST:
        lat = request.POST['lat']
        lng = request.POST['lng']
        petrol_bunks = Assistance.objects.filter(type='Petrol Bunk')
        mechanics = Assistance.objects.filter(type='Mechanic')
        for petrol_bunk in petrol_bunks:
            distance = get_distance(float(lat),float(lng),float(petrol_bunk.lat),float(petrol_bunk.lng))
            if distance <=5:
                petrol_bunk.distance = distance
                petrol_bunk.url = "https://www.google.com/maps/search/?api=1&query="+petrol_bunk.lat+","+petrol_bunk.lng
                nearby_petrol_bunks.append(petrol_bunk)
        for mechanic in mechanics:
            distance = get_distance(float(lat),float(lng),float(mechanic.lat),float(mechanic.lng))
            if distance <=5:
                mechanic.distance = distance
                mechanic.url = "https://www.google.com/maps/search/?api=1&query="+mechanic.lat+","+mechanic.lng
                nearby_mechanics.append(mechanic)
    params = {
        'petrol_bunks': nearby_petrol_bunks,
        'mechanics': nearby_mechanics
    }
    return render(request, 'index.html', params)