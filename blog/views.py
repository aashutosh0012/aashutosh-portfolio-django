from django.shortcuts import render

#import login_required decorator to require login before executing functions
from django.contrib.auth.decorators import login_required 
#Add in settings.py  LOGIN_URL='login/', or in view function @login_required(login_url='login/') 


#Import Post Class to display Posts from Databaase, created as Models
from .models import Post


#Django Built in Class based genric View
from django.views.generic import (ListView, DetailView, UpdateView, DeleteView, CreateView, UpdateView, DeleteView)


#LoginRequiredMixin is class based which requires authentication and un-authenticated users will be redirected to login, same as @login_required decorator(only works on functions)
#UserPassesTestMixin tests a function for any custom check, before running the class based view 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#This LoginRequiredMixin mixin should be at the leftmost position in the inheritance list


#---------------------------------------------------------------------------------------------------------------------#
def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

    # <!-- {{ request.META.get('HTTP_X_FORWARDED_FOR') }} -->
#---------------------------------------------------------------------------------------------------------------------#

# @login_required
def index(request):
	ip=visitor_ip_address(request)
	posts = ''
	data = {'posts':posts, 'ip':ip}
	return render(request,'blog/index.html', data)


#Blog Home View Function, Instead Use Class based view PostListView
# @login_required
# def home(request):
# 	posts = Post.objects.all()
# 	data = {'posts':posts}
# 	return render(request,'blog/blog_home.html', data)


# Desplay few Request info in about page
def about(request):
	username = request.user.username
	user = request.user
	ip=visitor_ip_address(request)
	all = request.META
	data = {'username':username, 'user':user, 'ip':ip, 'all':all}
	return render(request,'blog/about.html', data)



#---------------------------------------------------------------------------------------------------------------------#
#Class Based Views
#LoginRequiredMixin, class based decorator to login_required

#Create Class Based View "PostListView" from built-in "ListView" Class
class PostListView(LoginRequiredMixin, ListView):
	model = Post
	#default template for Class Based Views = <app>/<model>_<viewtype>.html
	template_name='blog/blog_home.html' 
	#default context variable name in class based view, context_object_name
	context_object_name='posts'
	ordering = ['-date_posted']   #List Posts in order=date_posted desc
	paginate_by = 5

class PostDetailView(LoginRequiredMixin, DetailView):
	model = Post
	#default template for Class Based Views = <app>/<model>_<viewtype>.html
	#template_name='blog/post_detail.html' 

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','content']
	#default template name for CreateView Class ='<app>/<model>_<form.html>'
	
	#pass user as author to instance of PostCreate form
	#assign current user as Post Author and run class built in form_valid method and pass current instance of form in form_valid
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#Define get_absolute_url method in Post Model Class, which will return reverse url string to post detail view or else

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title','content']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#Test Function for UserPassesTestMixin, it will check if User is the author of Post or not for updating
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True 
			
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	#Default Template Name blog/post_confirm_delete.html <app>/<model>_<confirm_delete.html>
	model = Post

	#Success/redicrect URL when Post is deleted successfully
	success_url = '/blog/'
	#success_url = "{% url 'blog-home' %}"
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True 
#---------------------------------------------------------------------------------------------------------------------#

#User Profile Posts, Profile view of Posts by a Users
#Return an object (user) and 404 Error if Object does not exists
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import  User
class UserPostListView(ListView):
	model = Post
	context_object_name='posts'
	template_name = 'blog/user_posts.html'
	paginate_by = 5
	def get_queryset(self):
		#get_object_or_404(Model,query)
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


#---------------------------------------------------------------------------------------------------------------------#


#Proejcts
#--------

from .models import Projects
def projects(request):
	projects = Projects.objects.all()
	context = {'projects':projects}
	print("1")
	return render(request,'blog/project_results.html', context)


def djangoProjects(request):
	projects = Projects.objects.filter(label__icontains="django")
	context = {'projects':projects}
	return render(request,'blog/project_results.html', context)

def pythonProjects(request):
	projects = Projects.objects.filter(label__icontains="python")
	context = {'projects':projects}
	return render(request,'blog/project_results.html', context)

def shellProjects(request):
	projects = Projects.objects.filter(label__icontains="shell")
	context = {'projects':projects}
	return render(request,'blog/project_results.html', context)

def allTechNews(request):
	return render(request,'blog/all-tech-news.html')

def youtubeVideoDownloader(request):
	return render(request,'blog/youtube-video-downloader.html')

def jiraSolarwindsIntegration(request):
	return render(request,'blog/jira-solarwinds-integration.html')