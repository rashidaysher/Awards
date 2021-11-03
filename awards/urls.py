from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views


urlpatterns=[
    url('^$',views.home,name='home'),
    url('awwards/project/(\d+)',views.rate_project,name='rate-project'),
    url('awwards/profile',views.view_profile,name='view-profile'),
    url('^search/', views.search_project, name='search_project'),
    url('^new/project$', views.new_project, name='new_project'),
    url('^awwardsapi/api/profile/$', views.ProfileList.as_view(),name='api-profile'),
    url('^awwardsapi/api/project/$', views.ProjectList.as_view(),name='api-project'),
    url('^awwardsapi/$',views.api_page,name='api-page'),
    url('register/',views.register, name='register'),
    url('^ratings/', include('star_ratings.urls', namespace='ratings')),
    # url('^awwardsapi/api/register/$', views.RegisterAPIView.as_view(),name='api-project'),

  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  