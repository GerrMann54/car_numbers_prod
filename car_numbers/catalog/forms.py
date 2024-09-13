from django import forms
from django.contrib.admin.utils import label_for_field
from django.core.exceptions import ValidationError
from .models import *

class PlateCreateForm(forms.ModelForm):
    class Meta:
        model = Plate
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get('number')
        region = cleaned_data.get('region')
        if Plate.objects.filter(number=number).filter(region=region):
            raise ValidationError('Такой номер уже существует')

class SearchForm(forms.Form):
    query = forms.CharField(max_length=6, label='Поиск номера')
