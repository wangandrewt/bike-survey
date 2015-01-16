from django import forms
from django.core.exceptions import ValidationError

from bikesurvey.models import SurveyInstance, Biker


class WelcomeForm(forms.Form):
    # from http://stackoverflow.com/a/1406012
    I_have_read_and_understand_the_instructions_above = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),
        choices=((1, 'Yes'), (0, 'No')),
        widget=forms.RadioSelect
    )


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

