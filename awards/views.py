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
