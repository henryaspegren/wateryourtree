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
  print location_name
  location = get_object_or_404(Location, name=location_name)
  return render_location(location)

def list(request):
  locations = Location.objects.order_by('-date_created')
  return render_locations(locations)


def hit(request, location_url, user_name):
  print location_url
  print user_name
  location = get_object_or_404(Location, url=location_url)
  room.topic('Fertilizer Update!')
  room.message(user_name+' has fertilized the '+str(location)+' tree (poo)', 'green', True, 'text')
  location.last_watered = datetime.datetime.now()
  location.hit_count += 1
  location.save()
  return render(request, 'index.html')

@csrf_exempt
def create_location(request):
  if request.method == 'POST':
    print request.POST
    name = request.POST['Location']
    print "NAME= " + str(name)
    if name is None:
      return HttpResponse(status=400)
    location = Location(name=name)
    location.save()
  return HttpResponseRedirect('/fertilizer/index.html#/create')

@csrf_exempt
def update_latitude(request):
  print request.POST
  location_url = request.POST['url_link']
  lat = request.POST['lat_update']
  print 'URL: '+ location_url + '    LAT: '+ lat
  location = get_object_or_404(Location, url=location_url)
  print "found location:" + str(location)
  location.lat = float(lat)
  location.save()

@csrf_exempt
def update_longitude(request):
  print request.POST
  location_url = request.POST['url_link']
  lng = request.POST['lng_update']
  print 'URL: '+ location_url + '    LNG: '+ lng
  location = get_object_or_404(Location, url=location_url)
  print "found location:" + str(location)
  location.lng = float(lng)
  location.save()
