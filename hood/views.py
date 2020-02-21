from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Posts,Profile,Neighbourhood,Business
from django.http import Http404
from .forms import BusinessForm,PostsForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
 

# Create your views here.
def index(request):
    hoods = Neighbourhood.objects.all()
    
    return render(request,'index.html',{"hoods":hoods})


@login_required(login_url='/accounts/login/')
def single_hood(request,location):
 
    location = Neighbourhood.objects.get(name=location) 
    print(location.id)
    businesses = Business.get_location_businesses(location.id) 
    posts = Posts.objects.filter(id=location.id) 
    print(posts)
   
    business_form = BusinessForm(request.POST)
    if request.method == 'POST':
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = request.user
            business.location = location
            business.save()
        return redirect('single_hood',location)
    
    else:
        business_form = BusinessForm()
        
    
    posts_form = PostsForm(request.POST)
    if request.method == 'POST':
        if posts_form.is_valid():
            form = posts_form.save(commit=False)
            form.user = request.user
            form.location = location
            form.save_post()
        return redirect('single_hood',location)
    
    else:
        posts_form = PostsForm()  
        
    context = {"location":location,
               "businesses":businesses,
               'business_form':business_form,
               "posts_form":posts_form,
                "posts":posts,
                }
    
    
    return render(request,'hood.html',context)