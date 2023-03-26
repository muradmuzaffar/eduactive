from django.shortcuts import render, get_object_or_404,redirect
from .models import University,Blogs,Scholarship,Apply
from .filters import ListingFiLtersUniversity,ListingFiLtersScholarship
from .forms import AdmissionForm,ContactForm,ApplyForm
from django.contrib.auth.decorators import login_required


def landing(request):


    if request.method == "POST":
        
        
        if 'applyBtn' in request.POST:
            form1 = AdmissionForm(request.POST)
            if form1.is_valid():

                gpa = form1.cleaned_data['gpa']
                degree = form1.cleaned_data['degree']
                study_field = form1.cleaned_data['study_field']
                region = form1.cleaned_data['region']
                ielts = form1.cleaned_data['ielts']
                toefl = form1.cleaned_data['toefl']
                gmat = form1.cleaned_data['gmat']
                gre = form1.cleaned_data['gre']

                



                if form1.cleaned_data['ielts']:
                    universities = University.objects.filter(gpa__lte =gpa , ielts__lte = ielts,degree =degree,
                                                         region=region,study_field = study_field )
                
                elif form1.cleaned_data['ielts'] and form1.cleaned_data['gre']:
                    universities = University.objects.filter(gpa__lte =gpa , ielts__lte = ielts,degree =degree,
                                                         region=region,gre__lte = gre,study_field = study_field )
                
                elif form1.cleaned_data['ielts'] and form1.cleaned_data['gmat']:
                    universities = University.objects.filter(gpa__lte =gpa , ielts__lte = ielts,degree =degree,
                                                         region=region,gmat__lte = gmat,study_field = study_field )

                elif form1.cleaned_data['toefl']:
                    universities = University.objects.filter(gpa__lte =gpa , toefl__lte = toefl,degree =degree,
                                                         region=region,study_field = study_field )
                
                elif form1.cleaned_data['toefl'] and form1.cleaned_data['gre']:
                    universities = University.objects.filter(gpa__lte =gpa , toefl__lte = toefl,degree =degree,
                                                         region=region,gre__lte = gre,study_field = study_field )
                
                elif form1.cleaned_data['toefl'] and form1.cleaned_data['gmat']:
                    universities = University.objects.filter(gpa__lte =gpa , toefl__lte = toefl,degree =degree,
                                                         region=region,gmat__lte = gmat,study_field = study_field )

                
                universities = universities.order_by('qs_rank')
                context = {
                    'universities':universities[0:5]

                }
                return render(request,'apply-request.html',context)
            else:
                return redirect('blogs')

            
           
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
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    print(request.user.email)
    if request.method == 'POST':
        Apply.objects.create(email = request.user.email)
        print('***************')
        print(request.user.email)

        return redirect('landing')
    else:
        return redirect('blogs')
    
    return render(request, 'apply-request.html')

@login_required(login_url = 'authenticate')
def apply_form(request):
    
    if request.method== 'POST':
            form = ApplyForm(request.POST)
            if form.is_valid():
                print('valid')
                form.save()
                return redirect("apply_done")
    
    form = ApplyForm()
            
    return render(request,'apply-form.html',{'form':form})


def apply_done(request):
    return render(request,'apply-done.html')

def universities(request):
    universities = University.objects.all()
    filter_university = ListingFiLtersUniversity(request.GET, queryset=universities)



    context  = {
        'universities':universities,
        'filter_university':filter_university,
    }
    return render(request,'universities.html',context)












def scholarships(request):
    scholarships = Scholarship.objects.all()
    filter_scholarship = ListingFiLtersScholarship(request.GET, queryset=scholarships)

    context = {
        'scholarships': scholarships,
        'filter_scholarship':filter_scholarship
    }
    return render(request, 'scholarships.html',context)


@login_required(login_url = 'authenticate')
def detail(request, id):

    
    university = get_object_or_404(University, id=id)
    if request.method == 'POST':
        Apply.objects.create(first_name = request.user.first_name,last_name = request.user.last_name,email = request.user.email,university_name = university.name,
                             program = university.program,gpa = request.user.profile.gpa,gre = request.user.profile.gre,
                             ielts = request.user.profile.ielts,toefl = request.user.profile.toefl,gmat = request.user.profile.gmat,number = request.user.profile.phone_number)
        return redirect('apply_done')
    return render(request, 'university-detail.html', {'university': university})


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

