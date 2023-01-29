from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('register', register, name='register'),
    path('login', log_in, name='log_in'),
    path('logout',log_out,name='log_out'),

    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_Sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),


    path('change_password/',MyPasswordChangeView.as_view(),name='change_password'),
    path('change_password_complete/',MyPasswordResetDoneView.as_view(),name='change_password_complete'),



]
