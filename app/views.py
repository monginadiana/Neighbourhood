from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from app.forms import CreateNeighForm, ProfileForm, UpdateProfileForm
from app.models import Profile

@login_required(login_url="/accounts/login/")
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, "profile.html", {"profile": profile})

@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile')
    return render(request, 'update_profile.html', {"form":form})

@login_required(login_url="/accounts/login/")
def create_hood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = CreateNeighForm(request.POST, request.FILES)
        if hood_form.is_valid():

            hood = hood_form.save(commit=False)
            hood.user = current_user
            hood.save()
        
        return HttpResponseRedirect('/profile')

    else:
        hood_form = CreateNeighForm()


    context = {'hood_form':hood_form}
    return render(request, 'create_hood.html',context)

@login_required(login_url="/accounts/login/")
def hoods(request):
    current_user = request.user
    hood = NeighbourHood.objects.all().order_by('-id')

    context ={'hood':hood}
    return render(request, 'hood.html', context)

@login_required(login_url='/accounts/login/')
def single_hood(request,neighbourHood_name):
    hood = NeighbourHood.objects.get(neighbourHood_name=neighbourHood_name)
    
    return render(request,'single_hood.html',{'hood':hood})