from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from app.forms import BusinessForm, CreateNeighForm, PostForm, ProfileForm, UpdateProfileForm
from app.models import Profile

@login_required(login_url="/accounts/login/")
def index(request):
    return render(request, 'index.html')

# @login_required(login_url='/accounts/login/')
# def create_profile(request):
#     current_user = request.user
#     title = "Create Profile"
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = current_user
#             profile.save()
#         return HttpResponseRedirect('/')
#     else:
#         form = ProfileForm()
#     return render(request, 'create_profile.html', {"form": form, "title": title})

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
    posts = Post.objects.filter(neighborhood=hood)
    businesses = Business.objects.filter(neighborhood=hood)
    return render(request,'single_hood.html',{'hood':hood, 'posts':posts, 'businesses':businesses})

def join_hood(request,id):
    neighborhood = get_object_or_404(NeighbourHood, id=id)
    
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('hood')

def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('hood')

@login_required(login_url="/accounts/login/")
def create_business(request):
    current_user = request.user
    if request.method == "POST":
        
        form=BusinessForm(request.POST,request.FILES)

        if form.is_valid():
            business=form.save(commit=False)
            business.user=current_user
            business.hood= hoods
            business.save()
        return HttpResponseRedirect('/businesses')
    else:
        form=BusinessForm()
    return render (request,'business_form.html', {'form': form, 'profile': profile})




@login_required(login_url="/accounts/login/")
def businesses(request):
    current_user = request.user
    businesses = Business.objects.all().order_by('-id')
    
    profile = Profile.objects.filter(user_id=current_user.id).first()

    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()
        
        locations = Location.objects.all()
        neighborhood = NeighbourHood.objects.all()
        
        businesses = Business.objects.all().order_by('-id')
        
        return render(request, "profile.html", {"danger": "Update Profile", "locations": locations, "neighborhood": neighborhood, "businesses": businesses})
    else:
        neighborhood = profile.neighborhood
        businesses = Business.objects.all().order_by('-id')
        return render(request, "business.html", {"businesses": businesses})
    
login_required(login_url="/accounts/login/")
def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hoods
            post.user=current_user
            post.save()
            return redirect('/posts')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


def posts(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    posts = Post.objects.filter(user_id=current_user.id)
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first() 
        posts = Post.objects.filter(user_id=current_user.id)
        
        locations = Location.objects.all()
        neighborhood = NeighbourHood.objects.all()
        
        businesses = Business.objects.filter(user_id=current_user.id)
        
        return render(request, "profile.html", {"danger": "Update Profile ", "locations": locations, "neighborhood": neighborhood,  "businesses": businesses,"posts": posts})
    else:
        neighborhood = profile.neighborhood
        posts = Post.objects.filter(user_id=current_user.id)
        return render(request, "post.html", {"posts": posts})
    
@login_required(login_url="/accounts/login/")
def search_business(request):
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_businesses = Business.objects.filter(name__icontains=search_term)
        message = f"Search For: {search_term}"

        return render(request, "search.html", {"message": message, "businesses": searched_businesses})
    else:
        message = "You haven't searched for any term"
        return render(request, "search.html", {"message": message})