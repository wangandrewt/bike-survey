from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect

from bikesurvey.models import SurveyInstance, Biker
import forms


# View all SurveyInstances
def list(request):
    list = SurveyInstance.objects.all()

    bikers = set()
    for biker in list[0].biker_set.all():
        bikers.add(biker)
        

    context = {'list': list, 'bikers': bikers}
    return render(request, 'bikesurvey/list.html', context)


# Create one SurveyInstance
def AddSurveyInstanceView(request):
    if request.method == "POST":
        # create a form instance with data from the request
        form = forms.SurveyInstanceForm(request.POST)
        if form.is_valid():
            p = form.save()
            return render(request, 'bikesurvey/detail.html', {
                'surveyinstance': p,
                'error_message': "",
            })
    else: # create a blank form
        form = forms.SurveyInstanceForm()

    return render(request, "bikesurvey/create.html", {'form': form})


# Add a Biker to a SurveyInstance
def AddBikerView(request, surveyInstance_id):
    p = get_object_or_404(SurveyInstance, pk=surveyInstance_id)
    if request.method == "POST":
        # create a form instance with data from the request
        form = forms.BikerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'bikesurvey/detail.html', {
                'surveyinstance': p,
                'form': form,
                'error_message': "",
            })
    else: # create a blank form
        form = forms.BikerForm()

    return render(request, "bikesurvey/detail.html", {
        'form': form,
        'surveyinstance': p,
    })


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
