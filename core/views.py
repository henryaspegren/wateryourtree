from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Fertilizer.utils import render_location, render_locations
from core.models import Location
import datetime
import hypchat

hc = hypchat.HypChat('iWtfWzxBZBgla9Q5nl19WJKTTiZh3nTEoyOIAMfx')
room = hc.get_room('Fertilizer Testing Room')

def index(request):
  return render(request, 'index.html')

def detail_json(request, location_url):
  location = get_object_or_404(Location, url=location_url)
  return render_location(location)

def name_json(request, location_name):
  location = get_object_or_404(Location, url=location_name)
  return render_location(location)

def list(request):
  locations = Location.objects.order_by('-date_created')
  return render_locations(locations)

def hit(request, location_url):
  location = get_object_or_404(Location, url=location_url)
  data = {}
  room.topic('Fertilizer Update!')
  room.message('The '+ str(location)+' tree has been fertilized (poo)', 'green', True, 'text')
  location.last_watered = datetime.datetime.now()
  location.hit_count += 1
  location.save()
  data = {'location':str(location), 'hits':str(location.hit_count)}

  return render(request, 'landing.html', data)

@csrf_exempt
def create_location(request):
  if request.method == 'POST':
    location = Location(name=request.POST['Location'])
    location.save()
  return HttpResponseRedirect('/')
