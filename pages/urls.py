from django.urls import path
from .views import *


urlpatterns = [

    path('university/detail/<int:id>', detail, name='detail'),
    path('filters', filters, name='filters'),
    path('blogs', blogs, name='blogs'),
    path('blogs/detail/<int:id>', blogs_detail, name='blogs_detail'),
    path('scholarships', scholarships, name='scholarships'),
    path('scholarship/detail/<int:id>', scholarship_detail, name='scholarship_detail'),
    path('apply-request', apply_request, name='apply_request'),
    path('apply-done', apply_done, name='apply_done'),
    path('apply-form', apply_form, name='apply_form'),
    

]
