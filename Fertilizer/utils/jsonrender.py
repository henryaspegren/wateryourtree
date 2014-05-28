from json import dumps
from django.http import HttpResponse

def render_location(location):
  json_location = dumps(location.to_json(), indent=2, separators=(',', ': '))
  return render_json(json_location)

def render_locations(locations):
  json_locations = []
  for location in locations:
    json_location = location.to_json()
    json_locations.append(json_location)

  json_locations = dumps(json_locations, indent=2, separators=(',', ': '))
  return render_json(json_locations)

def render_json(json_data):
  response = HttpResponse(json_data, content_type='application/json', status=200)
  return response
