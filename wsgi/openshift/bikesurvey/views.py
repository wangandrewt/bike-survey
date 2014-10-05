from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect

from bikesurvey.models import SurveyInstance, Biker
import forms


# Create one SurveyInstance
def AddSurveyInstanceView(request):
    if request.method == "POST":
        form = forms.SurveyInstanceForm(request.POST)
        if form.is_valid():
            p = form.save()
            p.biker_set.create(bikerGender='Male', bikerHelmet='Yes', bikerLocation='Street')
            p.biker_set.create(bikerGender='Male', bikerHelmet='Yes', bikerLocation='Sidewalk')
            p.biker_set.create(bikerGender='Male', bikerHelmet='No', bikerLocation='Street')
            p.biker_set.create(bikerGender='Male', bikerHelmet='No', bikerLocation='Sidewalk')
            p.biker_set.create(bikerGender='Female', bikerHelmet='Yes', bikerLocation='Street')
            p.biker_set.create(bikerGender='Female', bikerHelmet='Yes', bikerLocation='Sidewalk')
            p.biker_set.create(bikerGender='Female', bikerHelmet='No', bikerLocation='Street')
            p.biker_set.create(bikerGender='Female', bikerHelmet='No', bikerLocation='Sidewalk')
            return render(request, 'bikesurvey/detail.html', {
                'surveyinstance': p,
                'error_message': "",
            })
    else:
        form = forms.SurveyInstanceForm()

    return render(request, "bikesurvey/create.html", {'form': form})


# View one SurveyInstance
class DetailView(generic.DetailView):
    model = SurveyInstance
    template_name = 'bikesurvey/detail.html'


# Record Biker info into a SurveyInstance
def record(request, surveyInstance_id):
    p = get_object_or_404(SurveyInstance, pk=surveyInstance_id)
    try:
        selected_choice = p.biker_set.get(pk=request.POST['biker'])
    except (KeyError, Biker.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'bikesurvey/detail.html', {
            'surveyinstance': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.count += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'bikesurvey/detail.html', {
            'surveyinstance': p,
            'error_message': "This biker's info was recorded.",
        })
