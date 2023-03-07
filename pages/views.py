from django.shortcuts import render, get_object_or_404,redirect
from .models import University,Blogs,Scholarship
from .filters import ListingFiLters,ListingFiLtersScholarship
from .forms import AdmissionForm,ContactForm,ApplyForm
from django.contrib.auth.decorators import login_required

ielts = 0
gre = 0
gmat = 0
toefl = 0
def landing(request):


    if request.method == "POST":
        
        if 'applyBtn' in request.POST:
            form1 = AdmissionForm(request.POST)
            if form1.is_valid():

                gpa = form1.cleaned_data['gpa']
                degree = form1.cleaned_data['degree']

                if form1.cleaned_data['ielts']:
                    global ielts
                    ielts = form1.cleaned_data['ielts']
                
                if form1.cleaned_data['gre']:
                    global gre
                    gre = form1.cleaned_data['gre']
                
                if form1.cleaned_data['gmat']:
                    global gmat
                    gmat = form1.cleaned_data['gmat']

                if form1.cleaned_data['toefl']:
                    global toefl
                    toefl = form1.cleaned_data['toefl']
                print(gmat)
                print(gre)
                universities = University.objects.filter(gpa__gte =gpa , ielts__gte = ielts, gmat__gte = gmat,
                                                         gre__gte = gre,toefl__gte = toefl,degree =degree)
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
    return render(request, 'apply-request.html')



def apply_form(request):
    
    if request.method== 'POST':
            form = ApplyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("landing")
    
    form = ApplyForm()
            
    return render(request,'apply-form.html',{'form':form})


def apply_done(request):
    return render(request,'apply_done.html')












def scholarships(request):
    scholarships = Scholarship.objects.all()
    filter_scholarship = ListingFiLtersScholarship(request.GET, queryset=scholarships)

    context = {
        'scholarships': scholarships,
        'filter_scholarship':filter_scholarship
    }
    return render(request, 'scholarships.html',context)


# @login_required(login_url = 'log_in')
def detail(request, id):
    university = get_object_or_404(University, id=id)
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

