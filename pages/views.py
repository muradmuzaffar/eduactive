from django.shortcuts import render, get_object_or_404,redirect
from .models import University, Admission,Blogs,Scholarship
from .filters import ListingFiLters,ListingFiLtersScholarship
from .forms import AdmissionForm,ContactForm
from django.contrib.auth.decorators import login_required

# import pandas as pd
# import numpy as np
# from sklearn.ensemble import RandomForestRegressor
# import pickle
# Create your views here.

def landing(request):
    

    if request.method == "POST":
        
        if 'applyBtn' in request.POST:
            form1 = AdmissionForm(request.POST)
            if form1.is_valid():
                
                gpa = form1.cleaned_data['gpa']
                ielts = form1.cleaned_data['ielts']
                # print('****************')
                print(gpa)
                universities = University.objects.filter(ielts__gte =ielts)

                # print('*******************************')
                # universities = universities.order_by('-qs_rank')[0:3]
                # print(universities)
                request.session['universities'] = universities
                # return redirect("apply_request")
            
            


           
        if 'contactBtn' in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("landing")
            

    form = ContactForm()
    form1 = AdmissionForm()

    context = {
        'form':form,
        'form1':form1,

    }

    return render(request, 'index.html', context)



def apply_request(request):
    universities = request.session.get('universities')
    print('*******************************')
    print(universities)

    context = {
        'universities':universities,

    }
    
    return render(request, 'apply-request.html',context)
















def scholarships(request):
    scholarships = Scholarship.objects.all()
    filter_scholarship = ListingFiLtersScholarship(request.GET, queryset=scholarships)

    context = {
        'scholarships': scholarships,
        'filter_scholarship':filter_scholarship
    }
    return render(request, 'scholarships.html',context)


@login_required(login_url = 'log_in')
def detail(request, id):
    university = get_object_or_404(University, id=id)
    return render(request, 'detail.html', {'university': university})


def filters(request,):
    universitys = University.objects.all()
    filters = ListingFiLters(request.GET, queryset=universitys)
    # university = get_object_or_404(University, id=id)

    context = {
        'filters': filters,
        'form': filters.form,
        # 'university':university,
    }

    return render(request, 'filters.html', context)





def blogs(request):
    blogs = Blogs.objects.all()

    context = {
        'blogs': blogs
        }
    return render(request,'blogs.html',context)


def blogs_detail(request,id):
    blog = get_object_or_404(Blogs, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})

def scholarship_detail(request,id):
    scholarship = get_object_or_404(Scholarship, id=id)
    return render(request, 'scholarship_detail.html', {'scholarship': scholarship})

