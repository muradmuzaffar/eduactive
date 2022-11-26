import django_filters

from .models import University


class ListingFiLters(django_filters.FilterSet):
    class Meta:
        model = University
        fields = {
            'fee_waiver': ['exact'],
            'evaluation':  ['exact'],
            'degree':  ['exact'],
            
        }
