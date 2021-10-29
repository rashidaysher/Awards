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