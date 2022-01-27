from django_filters import FilterSet, DateFromToRangeFilter, CharFilter
from django_filters.widgets import RangeWidget
from .models import *


class SearchFilter(FilterSet):
    # author__author__username = CharFilter(label='Search by Author')
    dateCreation = DateFromToRangeFilter(
        widget=RangeWidget(
            attrs={'placeholder': 'YYYY-MM-DD'}))


    class Meta:
        model = Post

        fields = {'author__author__username': ['icontains'],}



