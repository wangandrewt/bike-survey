from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from bikesurvey.models import SurveyInstance, Biker


def index(request):
    latest_surveyInstance_list = SurveyInstance.objects.order_by('-date')[:5]
    output = ', '.join([p.name for p in latest_surveyInstance_list])
    return HttpResponse(output)

# Viewing one SurveyInstance
#def detail(request, surveyInstance_id):
 #   surveyInstance = get_object_or_404(SurveyInstance, pk=surveyInstance_id)
  #  return render(request, 'bikesurvey/detail.html', {'surveyInstance': surveyInstance})

class DetailView(generic.DetailView):
    model = SurveyInstance
    template_name = 'bikesurvey/detail.html'

class ResultsView(generic.DetailView):
    model = SurveyInstance
    template_name = 'bikesurvey/detail.html'

def record(request, surveyInstance_id):
    p = get_object_or_404(SurveyInstance, pk=surveyInstance_id)
    try:
        selected_choice = p.biker_set.get(pk=request.POST['biker'])
    except (KeyError, Biker.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'bikesurvey/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.count += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('bikesurvey:detail', args=(p.id,)))
