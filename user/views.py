from django.shortcuts import render, redirect

#import messages, to display successful form submission, user creaation
from django.contrib import  messages

#Import Custom Signup Form created with class name 'SignUpForm' in myapp/user/forms.py 
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm


#import login_required decorator to require login before executing functions
from django.contrib.auth.decorators import login_required 
#Add in settings.py  LOGIN_URL='login/', or in view function @login_required(login_url='login/') 




from django.contrib.auth import logout

def home(request):
	data = {}
	return render(request,'user/user_home.html')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			#Check for messages
			messages.success(request, f'Account created for {username}, Please Login!')
			return redirect('login')
	else:
		form = SignUpForm()

	data = {'form': form, 'messages':messages}
	return render(request,'user/signup.html',data)

# def logout_view(request):
# 	logout(request)
# 	return render('user/logout.html')

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Account updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {'u_form':u_form,'p_form':p_form}
	return render(request,'user/profile.html', context)
