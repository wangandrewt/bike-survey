from django import forms
from django.core.exceptions import ValidationError

from bikesurvey.models import SurveyInstance


class SurveyInstanceForm(forms.ModelForm):

    class Meta:
        model = SurveyInstance

