from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from Fertilizer.utils import render_location, render_locations
from core.models import Location

import hypchat

hc = hypchat.HypChat('HMKmVOnIKudLTskiuZfosszhed4cRX4S9TeFb3s2')

def index(request):
  return render(request, 'index.html')

def detail_json(request, location_url):
  location = get_object_or_404(Location, url=location_url)
  return render_location(location)

def list(request):
  locations = Location.objects.order_by('-date_created')
  return render_locations(locations)

def hit(request, location_url):
  location = get_object_or_404(Location, url=location_url)

  me = hc.get_user("mgeist@betterworks.com")
  me.message('(poo) - ' + location.name)

  location.hit_count += 1
  location.save()

@csrf_exempt
def create_location(request):
  if request.method == 'POST':
    location = Location(name=request.POST['Location'])
    location.save()
    return redirect('/fertilizer/location.html')
