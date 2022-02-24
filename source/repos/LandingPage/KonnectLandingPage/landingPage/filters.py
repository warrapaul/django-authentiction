import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
   




	class Meta:
		model = feed
		fields = ['Categories','title','subtitle','slug',]
		exclude = ['body','meta_description','date_created','date_modified','year_Created','publish_date','published','tags','']


