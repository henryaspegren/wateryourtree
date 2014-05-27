from django.db import models
from django.db.models.signals import pre_save
import base64
import datetime

# Create your models here.
class Location(models.Model):
  url = models.CharField(max_length=100)
  name = models.CharField(max_length=50)
  hit_count = models.IntegerField(default=0)
  date_created = models.DateTimeField('date created', default=datetime.datetime.now())

  def __unicode__(self):
    return self.name


def pre_location_save(sender, instance, **kwargs):
  instance.url = base64.b64encode(instance.name)

pre_save.connect(pre_location_save, sender=Location)
