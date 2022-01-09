
from django.contrib import admin
from .models import Business, Post, Profile, NeighbourHood, Location


# Register your models here.
admin.site.register(Profile)
admin.site.register(NeighbourHood)
admin.site.register(Location)
admin.site.register(Business)
admin.site.register(Post)