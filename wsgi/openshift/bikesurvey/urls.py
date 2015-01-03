from django.conf.urls import patterns, url

from bikesurvey import views

urlpatterns = patterns('',
    # ex: /bikesurvey/
    url(r'^$', views.AddSurveyInstanceView, name='index'),
    # ex: /bikesurvey/list/
    url(r'^list/$', views.list, name='list'),
    # ex: /bikesurvey/5/record/
    url(r'^(?P<surveyInstance_id>\d+)/record/$', views.record, name='record'),
    # ex: /bikesurvey/5/
    url(r'^(?P<surveyInstance_id>\d+)/$', views.AddBikerView, name='detail'),
)
