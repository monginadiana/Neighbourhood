from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def save_location(self):
        self.save()
    def __str__(self):
        return self.name

class NeighbourHood(models.Model):
    image= CloudinaryField("image",null=True, blank=True)
    neighbourHood_name = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    occupants_count = models.IntegerField(default=0, null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    
    def create_neigbourhood(self):
        self.save()
    
    @classmethod
    def delete_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()
    
    @classmethod
    def update_neighbourhood(cls, id):
        cls.objects.filter(id=id).update()
    
    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood
    
    @classmethod
    def find_neigbourhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    profile_photo = CloudinaryField("image",null=True, blank=True)
    bio = models.TextField(max_length=300)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=100,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    
    def save_profile(self):
        self.save()
    
    def create_profile(self):
        self.save()
    
    def update_profile(self):
        self.save()
   
    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile
    def __str__(self):
        return self.user.username