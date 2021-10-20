from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from instagram.views import home,new_comment,profile,search_results
from django.urls import path,include


urlpatterns=[
    url('^$',views.home,name= 'welcome'),
    url(r'^new/comment$', views.new_comment, name='new_comment'),
    url(r'^profile/user$', views.profile, name='profile'),
    path('search/', search_results, name='search_results')

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)