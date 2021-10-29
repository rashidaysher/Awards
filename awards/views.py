from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,Rating
from .forms import NewProjectForm,ProfileUpdateForm,RatingsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer


# Create your views here.
def home(request):
    projects= Project.objects.all()
    return render(request,'awardss/home.html', {'project':projects})

@login_required(login_url='/accounts/login/') 
def rate_project(request,id):
    project=Project.objects.get(id=id)

    ratings = Rating.objects.filter(user=request.user, id=id).first()
    rating_status = None
    if ratings is None:
        rating_status = False

    else:
        rating_status = True
    
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project
            rate.save()
            project_ratings = Rating.objects.filter(id=id)

            design_ratings = [d.design for d in project_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in project_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in project_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return  JsonResponse(request.path_info)
    
        else:
            form = RatingsForm()
        params = {
            'project': project,
            'rating_form': form,
            'rating_status': rating_status

    } 
    return render(request, 'awardss/project.html', params)

@login_required(login_url='/accounts/login/') 
def view_profile(request):
    projects=request.user.profile.project_set.all() 
    profile=request.user.profile    

    form=ProfileUpdateForm(instance=profile)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    context={
        'form':form,
        'projects':projects,
    }
    return render(request,"awardss/profile.html",context=context)

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user = User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        profile=Profile.objects.create(user=user,email=user.email)
        
        return redirect('login')
    else:
        return render(request,'registration/registration_form.html')    

@login_required(login_url='/accounts/login/') 
def search_project(request):
    if "project" in request.GET and request.GET["project"]:
        search_term=request.GET.get("project")
        searched_projects=Project.search_by_name(search_term)
        message = f"{search_term}"

        return render(request,'awardss/search.html',{"message":message, "projects":searched_projects, "project":search_term})
    
    else:
        message = "Please enter search name"

        return render(request, 'awardss/search.html',{"message":message})

@login_required(login_url='/accounts/login/')     
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
        
    else:
        form = NewProjectForm()
    return render(request, 'awardss/new_project.html', {"form":form, "current_user":current_user})

@login_required(login_url='/accounts/login/')   
def api_page(request):
    return render(request,'awardss/api_page.html')


class ProfileList(APIView):
    def get(self, request, fromat=None):
        all_profiles =Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


class ProjectList(APIView):
    def get(self, request, fromat=None):
        all_projects =Project.objects.all()
        serializers =ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
