from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('awardss/project/(\d+)',views.rate_project,name='rate-project'),
    path('awardss/profile',views.view_profile,name='view-profile'),
    path('search/', views.search_project, name='search_project'),
    path('new/project$', views.new_project, name='new_project'),
    path('awwardsapi/api/profile/$', views.ProfileList.as_view(),name='api-profile'),
    path('awwardsapi/api/project/$', views.ProjectList.as_view(),name='api-project'),
    path('awwardsapi/$',views.api_page,name='api-page'),
    path('register/',views.register, name='register'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)