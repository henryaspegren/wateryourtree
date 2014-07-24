from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Fertilizer.utils import render_location, render_locations, render_comments
from core.models import Location, Comment
from core.apis.yo import yo_all
from core.apis.hipchat import message_room
from django.utils import timezone
import json



HC_TOKEN = 'iWtfWzxBZBgla9Q5nl19WJKTTiZh3nTEoyOIAMfx'
HC_ROOM = 'Fertilizer Testing Room'
YO_TOKEN = '654ae0e2-4e98-aab4-628f-cdd108c59f37'


def index(request):
  return render(request, 'index.html')

def detail_json(request, location_url):
  location = get_object_or_404(Location, url=location_url)
  return render_location(location)

def name_json(request, location_name):
  location = get_object_or_404(Location, name=location_name)
  return render_location(location)

def list(request):
  locations = Location.objects.order_by('-date_created')
  return render_locations(locations)

def tree_comments(request, location_url):
  tree = get_object_or_404(Location, url=location_url)
  comments = Comment.objects.filter(associated_tree=tree).order_by('-date')
  return render_comments(comments)

def hit(request, location_url, user_name):
  location = get_object_or_404(Location, url=location_url)
  location.last_watered = timezone.now()
  location.hit_count += 1
  location.last_watered_name = str(user_name)
  location.save()

  # API Calls
  # message_room(HC_TOKEN, HC_ROOM, user_name, location)
  # yo_all(YO_TOKEN)
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
def create_comment(request):
  data = json.loads(request.body)
  name = data['name']
  tree_url = data['tree']
  comment = data['comment']
  if None in (name, tree_url, comment):
    return HttpResponse(status=400)
  associated_tree = get_object_or_404(Location, url=tree_url)
  newcomment = Comment(name=name, associated_tree=associated_tree, comment=comment)
  print newcomment
  newcomment.save()
  return HttpResponse(status=200)

@csrf_exempt
def update_latitude(request):
  location_url = request.POST['url_link']
  lat = request.POST['lat_update']
  location = get_object_or_404(Location, url=location_url)
  location.lat = float(lat)
  location.save()
  return HttpResponse(status=200)

@csrf_exempt
def update_longitude(request):
  location_url = request.POST['url_link']
  lng = request.POST['lng_update']
  location = get_object_or_404(Location, url=location_url)
  location.lng = float(lng)
  location.save()
  return HttpResponse(status=200)
