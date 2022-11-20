from django.urls import path, include
from .views import *


urlpatterns = [
    path('register', register, name='register'),
    path('login', log_in, name='log_in'),
    path('logout',log_out,name='log_out')

]
