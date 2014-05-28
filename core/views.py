from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from Fertilizer.utils import render_location, render_locations
from core.models import Location

import hypchat

hc = hypchat.HypChat("HMKmVOnIKudLTskiuZfosszhed4cRX4S9TeFb3s2")

# Create your views here.
def index(request):
  locations = Location.objects.order_by('-date_created')
  context = {'locations': locations}
  return render(request, 'core/index.html', context)

def detail_json(request, location_url):
  location = get_object_or_404(Location, url=location_url)
  return render_location(location)

def list(request):
  locations = Location.objects.order_by('-date_created')
  return render_locations(locations)

def hit(request, location_url):
  location = get_object_or_404(Location, url=location_url)

  me = hc.get_user("mgeist@betterworks.com")
  me.message("(poo) - " + location.name)

  location.hit_count += 1
  location.save()

def create_location(request):
  if request.method == 'POST':
    location = Location(name=request.POST['Location'])
    location.save()
