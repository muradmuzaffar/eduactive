from django.shortcuts import render
from .models import University
from .filters import ListingFiLters
# Create your views here.


def landing(request):
    universitys = University.objects.all()
    filters = ListingFiLters(request.GET,queryset=universitys)

    context = {
        'filters': filters
    }

    return render(request, 'landing.html', context)
