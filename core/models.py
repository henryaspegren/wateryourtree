from django.db import models
from django.db.models.signals import pre_save
import base64
import datetime
from calendar import timegm

# Create your models here.
class Location(models.Model):
  url = models.CharField(max_length=100)
  name = models.CharField(max_length=50, unique=True)
  hit_count = models.IntegerField(default=0)
  lat = models.DecimalField(default=37.42565, decimal_places=11, max_digits=15)
  lng = models.DecimalField(default=-122.13535, decimal_places=11, max_digits=15)
  last_watered = models.DateTimeField('date last watered', default=datetime.datetime.now())
  date_created = models.DateTimeField('date created', default=datetime.datetime.now())

  def __unicode__(self):
    return self.name

  def to_json(self):
    return {
     'url': self.url,
     'name': self.name,
      'hit_count': self.hit_count,
      'lat': str(self.lat),
      'lng': str(self.lng),
      'date_created': timegm(self.date_created.utctimetuple()),
      'last_watered': timegm(self.last_watered.utctimetuple())
    }


def pre_location_save(sender, instance, **kwargs):
  instance.url = base64.b64encode(instance.name)

pre_save.connect(pre_location_save, sender=Location)
