from django.urls import path, include
from .views import *


urlpatterns = [
    path('register', register, name='register'),
    path('login', log_in, name='log_in'),

]
