from django.shortcuts import render, get_object_or_404

from core.models import Location

import hypchat

hc = hypchat.HypChat("HMKmVOnIKudLTskiuZfosszhed4cRX4S9TeFb3s2")

# Create your views here.
def index(request):
  locations = Location.objects.order_by('-date_created')
  context = {'locations': locations}
  return render(request, 'core/index.html', context)

def detail(request, location_url):
  location = get_object_or_404(Location, url=location_url)

  me = hc.get_user("mgeist@betterworks.com")
  me.message("(poo) - " + location.name)

  context = {'location': location}
  return render(request, 'core/detail.html', context)
