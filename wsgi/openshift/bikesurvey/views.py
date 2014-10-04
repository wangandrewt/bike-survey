from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from bikesurvey.models import SurveyInstance


def index(request):
    latest_surveyInstance_list = SurveyInstance.objects.order_by('-date')[:5]
    output = ', '.join([p.name for p in latest_surveyInstance_list])
    return HttpResponse(output)

# Viewing one SurveyInstance
def detail(request, surveyInstance_id):
    surveyInstance = get_object_or_404(SurveyInstance, pk=surveyInstance_id)
    return render(request, 'bikesurvey/detail.html', {'surveyInstance': surveyInstance})

def record(request, surveyInstance_id):
    return HttpResponse("You're recording biker information on surveyInstance %s." % surveyInstance_id)
