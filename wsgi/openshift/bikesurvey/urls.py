from django.conf.urls import patterns, url

from bikesurvey import views

urlpatterns = patterns('',
    # ex: /bikesurvey/
    url(r'^$', views.index, name='index'),
    # ex: /bikesurvey/5/record/
    url(r'^(?P<surveyInstance_id>\d+)/record/$', views.record, name='record'),
    # ex: /bikesurvey/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
)