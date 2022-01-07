from .models import NeighbourHood, Profile
from django.forms import ModelForm
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo','contact','location','neighborhood')
    

class CreateNeighForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ['admin','occupants_count']