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
    universitys = University.objects.all()


    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            form.save()
            return redirect("landing")

    form = ContactForm()

    context = {
        'universitys': universitys,
        'form':form
    }

    return render(request, 'index.html', context)

def scholarships(request):
    scholarships = Scholarship.objects.all()
    filter_scholarship = ListingFiLtersScholarship(request.GET, queryset=scholarships)
    print(filter_scholarship.form)

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


def admission(request):
    form = AdmissionForm(request.POST or None)
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            gre = form.cleaned_data['gre']
            gpa = form.cleaned_data['gpa']
            lor = form.cleaned_data['lor']
            sop = form.cleaned_data['sop']
            research = form.cleaned_data['research']
            rating = form.cleaned_data['rating']
            toefl = form.cleaned_data['toefl']

            result_1 =  gpa*0.1+lor*0.2+sop*0.2
            result_2 = (gre/340) + (toefl/120)
            result_3 = float(research) - float(rating)*0.2
            print('***************************')

            final_result = (round((result_1+result_2+result_3) / 7 , 2)) 
            print('***************************')


            # inputs = pd.DataFrame({'gre': gre,
            #                        'toefl': toefl,
            #                        'university_rating': rating,
            #                        'sop': sop,
            #                        'lor': lor,
            #                        'gpa': gpa,
            #                        'research': research,

            #                        },  index=[0])
            # # print(inputs)
            # # print('****************************')

            # model = pd.read_pickle('./Model Design/model.pkl')

            # data = pd.read_csv('./Model Design/admission_data.csv',
            #                    index_col=0).drop(columns=['admit_chance']).reset_index()
            # # print(data)
            # # print('****************************')
            # df = pd.concat([inputs, data], axis=0)
            # # print(df)
            # # print('****************************')

            # encode = ['research', 'university_rating']
            # for col in encode:
            #     dummy = pd.get_dummies(df[col], prefix=col)
            #     df = pd.concat([df, dummy], axis=1)
            #     del df[col]
            # df = df[:1]
            # # del df['lor']
            # # df.columns = np.unique(df.columns)
            # df = df.loc[:,~df.columns.duplicated()].copy()
            
            # # print('****************************')
            # # print(df)
            # # print('****************************')


        
            # pred = model.predict(df)
            # # print(pred)
            

        return render(request, 'admission.html', {"pred": final_result})
    else:
        return render(request, 'admission.html', {'form': form})


def blogs(request):
    blogs = Blogs.objects.all()

    context = {
        'blogs': blogs
        }
    return render(request,'blogs.html',context)


def blogs_detail(request,id):
    blog = get_object_or_404(Blogs, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})
