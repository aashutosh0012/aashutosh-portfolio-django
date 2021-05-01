
#Use Signals to create Profiles automatically when a User is created.

#Import DJango's built in signal:post_save (pre_save,post_save,pre_delete,post_delete etc)
from django.db.models.signals import post_save

#import receiver decorator to connect recieving function to the signal
from django.dispatch import receiver

#Import User Model, which will be sender of signal
from django.contrib.auth.models import User

#import Profile model, to create new Profiles for new Users
from .models import Profile



@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	instance.profile.save()
