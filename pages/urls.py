from django.urls import path
from .views import *


urlpatterns = [

    path('university/detail/<int:id>', detail, name='detail'),
    path('filters', filters, name='filters'),
    path('admission', admission, name='admission'),
    path('blogs', blogs, name='blogs'),
    path('scholarships', scholarships, name='scholarships'),
    path('blogs/detail/<int:id>', blogs_detail, name='blogs_detail'),

]
