from django.contrib import admin
from core.models import Location, Comment

class LocationAdmin(admin.ModelAdmin):
  fields = ['name', 'lng', 'lat', 'url', 'hit_count']

class CommentAdmin(admin.ModelAdmin):
  fields = ['name', 'associated_tree', 'comment']

admin.site.register(Location, LocationAdmin)
admin.site.register(Comment, CommentAdmin)
