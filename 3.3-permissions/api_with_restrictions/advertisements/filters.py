from django_filters.rest_framework.filterset import FilterSet
from django_filters.filters import DateTimeFromToRangeFilter
from advertisements.models import Advertisement

class AdvertisementFilter(FilterSet):
    date_filter = DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Advertisement
        fields = ['status', 'creator', 'in_favourite__user']