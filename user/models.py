from django.db import models

# # Create your models here.
from django.contrib.auth.models import User


#Import PIL.Image to resize Profile Image
from PIL import  Image

# #Create a class for Profiles
class Profile(models.Model):
	#Creates a one to one Field for Profile and User, on_delete=models.CASCADE, deletes the Profile if User is deleted, not vice-versa
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
	#upload_to defined location of uploaded image, i.e. myapp/profile_pics

	#add below MEDIA_ROOT & MEDIA_URL in settings.py to upload images to media directory
	#Media Root= Directory full path, where uploaded files are stored
	# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
	# #Media URL is the public URL which browser will use to access media files
	# MEDIA_URL = '/media/'

	def __str__(self):
		return f'{self.user.username} Profile'


	#Define Save method of User Model Class, to resize the image when profile is saved
	def save(self):
		#Call parent class built in  Save method using super()
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)