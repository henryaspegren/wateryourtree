from django.contrib import admin
from core.models import Location

class LocationAdmin(admin.ModelAdmin):
  fields = ['name', 'lng', 'lat', 'url', 'hit_count']

admin.site.register(Location, LocationAdmin)
