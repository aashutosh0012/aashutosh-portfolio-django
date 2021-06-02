"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from user import views as user_views
from blog import views as blog_views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',blog_views.index, name='index'),
    # path('#',blog_views.home, name='blog-home'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('about/', blog_views.about, name="about"),
    path('projects/', blog_views.projects, name="projects"),
    path('', include('django.contrib.auth.urls'))
]


urlpatterns += [
    path('blog/',include('blog.urls')),
    path('user/',include('user.urls')),

    path('projects/django/', blog_views.djangoProjects, name="django-projects"),
    path('projects/python/', blog_views.pythonProjects, name="python-projects"),
    path('projects/shell/', blog_views.shellProjects, name="shell-projects"),
    path('projects/all-tech-news/', blog_views.allTechNews, name="all-tech-news"),
    path('projects/youtube-video-downloader/', blog_views.youtubeVideoDownloader, name="youtube-video-downloader"),
    path('projects/jira-solarwinds-integration-via-rest-api/', blog_views.jiraSolarwindsIntegration, name="jira-solarwinds-integration"),

]



#To Serve user uploaded media files, add this to urlpatterns, static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()