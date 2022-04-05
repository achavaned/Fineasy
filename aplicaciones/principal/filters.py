import django_filters
from django_filters import DateFilter

from django import forms
from .models import *

class DateInput(forms.DateInput):
    	input_type = 'date'

class CalendarIngresosFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=DateInput(attrs={'class': 'datepicker'}))
    class Meta:
        model = Ingreso
        fields = '__all__'
        exclude = ['nombre_ingreso','valor', 'categoria','tag','usuario']

class CalendarGastosFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=DateInput(attrs={'class': 'datepicker'}))
    class Meta:

        model = Gasto
        fields = '__all__'
        exclude = ['nombre_Gasto','valor', 'categoria','tag','usuario']
        
class TipoIngresosFilter(django_filters.FilterSet):
    class Meta:
        model = Ingreso
        fields = '__all__'
        exclude = ['nombre_ingreso','valor', 'categoria','date','usuario']
        
class TipoGastosFilter(django_filters.FilterSet):
    class Meta:
        model = Gasto
        fields = '__all__'
        exclude = ['nombre_Gasto','valor', 'categoria','date','usuario']