from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

#Proive reverse url to any path when a model is saved
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	#ForeignKey allows many to one relationship, all posts will belong to one user
	#on_delete=models.CASCADE, will delete the post, if user is deleted
	author = models.ForeignKey(User,on_delete=models.CASCADE)

	#Returns title name 
	def __str__(self):
		return self.title

	#Proive reverse url to post detail view 
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	















	# Models in Django are stored as Tables in Database with, Fields as respective Columns and datatype
	#run below commands to migrate changes to Database
	#python manage.py makemigrations
	#it will create migrations file, for which changes needs to be deployed in Database
	# [kumara6.BGLRLITOPS02] ➤ python3 manage.py makemigrations
	# 	Migrations for 'blog':
 	#  		blog/migrations/0001_initial.py
 	#    	- Create model Post
                       


 	#run sqlmigrate to generate SQL statement, which will be used to create table in Database for the Model
 	#python manage.py sqlmigrate <app_name> <migration_number>
	#python manage.py sqlmigrate blog 001

	#Migrate changes to Database
	#python manage.py migrate