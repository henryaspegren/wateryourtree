from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from Fertilizer.utils import render_location, render_locations
from core.models import Location
import datetime
import hypchat

hc = hypchat.HypChat('iWtfWzxBZBgla9Q5nl19WJKTTiZh3nTEoyOIAMfx')

def index(request):
  return render(request, 'index.html')

def detail_json(request, location_url):
  location = get_object_or_404(Location, url=location_url)
  return render_location(location)

def produce_detail_page(request, location_url):
  location = get_object_or_404(Location, url=location_url)
  data = {'name': str(location.name), 'hits':str(location.hit_count), 'lat':str(location.lat),
  'lng': str(location.lng), 'watered': str(location.last_watered), 'created': str(location.date_created),
  'url': location.url}
  return render(request, 'test.html', data)

def list(request):
  locations = Location.objects.order_by('-date_created')
  return render_locations(locations)

def hit(request, location_url):
  location = get_object_or_404(Location, url=location_url)

  me = hc.get_user("henry@betterworks.com")
  #me.message('(poo) - ' + location.name)

  location.hit_count += 1
  location.save()
  data = {'location':str(location), 'hits':str(location.hit_count)}

  return render(request, 'landing.html', data)

@csrf_exempt
def create_location(request):
  if request.method == 'POST':
    location = Location(name=request.POST['Location'])
    location.save()
    return render('/fertilizer/location.html')
