import requests

def yo_all(api_token):
  print "Yo'ing all users"
  return requests.post("http://api.justyo.co/yoall/", data={'api_token': api_token})
