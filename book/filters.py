from django_filters.rest_framework import FilterSet, DateFromToRangeFilter
from book.models import Book


class DateFilter(FilterSet):
    date_range = DateFromToRangeFilter(field_name="date", label='Date range')

    class Meta:
        model = Book
        fields = ['author', 'genre', 'date']
