from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect

from bikesurvey.models import SurveyInstance, Biker
import forms


# Welcome message
def IndexView(request):
    message = ""
    
    if request.method == 'POST':
        form = forms.WelcomeForm(request.POST)
        if form.is_valid():
            if (bool(int(form.cleaned_data
                    ['I_have_read_and_understand_the_instructions_above']))
                    == True):
                return redirect('bikesurvey:start')
    # create a blank form
    form = forms.WelcomeForm()
    
    return render(request, 'bikesurvey/welcome.html', {
        'form': form,
        'message': message
    })


# View all SurveyInstances
def ListView(request):
    results = Biker.objects.all()
    for biker in results:
        surveyInstance = biker.surveyInstance
        biker.name = surveyInstance.name
        biker.location = surveyInstance.location
        biker.date = surveyInstance.date

    return render(request, 'bikesurvey/list.html', {'list': results})


# Create one SurveyInstance
def AddSurveyInstanceView(request):
    message = ""
    
    if request.method == "POST":
        # create a form instance with data from the request
        form = forms.SurveyInstanceForm(request.POST)
        if form.is_valid():
            surveyInstance = form.save()
            return redirect('bikesurvey:detail', surveyInstance_id = surveyInstance.id)
    else: # create a blank form
        form = forms.SurveyInstanceForm()
    
    return render(request, "bikesurvey/create.html", {
        'form': form,
        'message': message
    })


# Add a Biker to a SurveyInstance
def AddBikerView(request, surveyInstance_id):
    surveyInstance = get_object_or_404(SurveyInstance, pk=surveyInstance_id)
    message = ""
    
    if request.method == "POST":
        # create a form instance with data from the request
        form = forms.BikerForm(request.POST)
        if form.is_valid():
            biker = form.save(commit=False)
            biker.surveyInstance = surveyInstance
            biker.save()
            message = "Biker added."
    
    # create a blank form
    form = forms.BikerForm()

    return render(request, "bikesurvey/detail.html", {
        'form': form,
        'surveyinstance': surveyInstance,
        'message': message,
    })

# Closing message
def ThanksView(request):
    return render(request, 'bikesurvey/thanks.html')
