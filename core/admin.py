from django.contrib import admin
from core.models import Location

class LocationAdmin(admin.ModelAdmin):
  fields = ['name']

admin.site.register(Location, LocationAdmin)
