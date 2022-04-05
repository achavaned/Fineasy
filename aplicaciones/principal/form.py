from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
class DateInput(forms.DateInput):
	input_type = 'date'
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class IngresoForm(ModelForm):
	class Meta:
		model = Ingreso
		fields = ['nombre_ingreso','valor', 'categoria','tag','date']
		widgets = {'date': DateInput()}
class GastoForm(ModelForm):
	class Meta:
		model = Gasto
		fields = ['nombre_Gasto','valor', 'categoria','tag','date']
		widgets = {'date': DateInput()}
class Profile(ModelForm):
	class Meta:
		model = User
		fields = ['username','email']