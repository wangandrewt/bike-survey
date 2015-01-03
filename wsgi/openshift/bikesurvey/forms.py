from django import forms
from django.core.exceptions import ValidationError

from bikesurvey.models import SurveyInstance, Biker


class SurveyInstanceForm(forms.ModelForm):

    class Meta:
        model = SurveyInstance
        fields = ['name', 'location', 'date']
        widgets = {
            'location': forms.Select,
        }


class BikerForm(forms.ModelForm):

    class Meta:
        model = Biker
        fields = ['bikerGender', 'bikerHelmet', 'bikerLocation']
        labels = {
            'bikerGender': 'Gender',
            'bikerHelmet': 'Helmet',
            'bikerLocation': 'Location',
        }
        widgets = {
            'bikerGender': forms.RadioSelect,
            'bikerHelmet': forms.RadioSelect,
            'bikerLocation': forms.RadioSelect,
        }

