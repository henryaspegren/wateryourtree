from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
import base64
import datetime

# Location Model
class Location(models.Model):
  url = models.CharField(max_length=100)
  name = models.CharField(max_length=50, unique=True)
  hit_count = models.IntegerField(default=0)
  lat = models.DecimalField(default=37.42565, decimal_places=11, max_digits=15)
  lng = models.DecimalField(default=-122.13535, decimal_places=11, max_digits=15)
  last_watered = models.DateTimeField('date last watered', default=timezone.now())
  last_watered_name = models.CharField(max_length=100, default='Not yet watered')
  date_created = models.DateTimeField('date created', default=timezone.now())

  def __unicode__(self):
    return self.name

  def to_json(self):
    return {
     'url': self.url,
     'name': self.name,
      'hit_count': self.hit_count,
      'lat': str(self.lat),
      'lng': str(self.lng),
      'date_created': str(self.date_created),
      'last_watered_name': str(self.last_watered_name),
      'last_watered': str(self.last_watered)
    }

# Comments Model
class Comment(models.Model):
  name = models.CharField(max_length=50)
  date = models.DateTimeField(default=timezone.now())
  associated_tree = models.ForeignKey('Location')
  comment = models.TextField()

  def __unicode__(self):
    return self.name+' '+str(self.date)

  def to_json(self):
    return {
      'name': self.name,
      'date': str(self.date),
      'associated_tree_name': self.associated_tree.name,
      'associated_tree_url': self.associated_tree.url,
      'comment': self.comment
    }



def pre_location_save(sender, instance, **kwargs):
  instance.url = base64.b64encode(instance.name)

pre_save.connect(pre_location_save, sender=Location)
