
from django.contrib import admin
from .models import Profile, NeighbourHood, Location


# Register your models here.
admin.site.register(Profile)
admin.site.register(NeighbourHood)
admin.site.register(Location)