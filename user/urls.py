from django.urls import path, include
from . import views

#import auth views for Password Reset Functionality
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='user-home'),
    path('signup/', views.signup, name='signup'),

    #Single auth_views.PasswordResetView.as_view() default in Django for Password Reset
    path('password-reset', auth_views.PasswordResetView.as_view(), name='password-reset'),
    #path('password-reset', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password-reset'),
    # path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset-done.html'), name='password-reset-done'),
]
