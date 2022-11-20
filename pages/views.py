from django.shortcuts import render, get_object_or_404
from .models import University
from .filters import ListingFiLters
# Create your views here.


def landing(request):
    universitys = University.objects.all()
    # filters = ListingFiLters(request.GET,queryset=universitys)

    context = {
        'universitys': universitys
    }

    return render(request, 'landing.html', context)


def detail(request, id):
    university = get_object_or_404(University, id=id)
    return render(request, 'detail.html', {'university': university})


def filters(request,):
    universitys = University.objects.all()
    filters = ListingFiLters(request.GET, queryset=universitys)
    # university = get_object_or_404(University, id=id)

    context = {
        'filters': filters,
        'form':filters.form,
        # 'university':university,
    }

    return render(request, 'filters.html', context)
