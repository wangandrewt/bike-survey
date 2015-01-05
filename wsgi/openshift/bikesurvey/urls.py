from django.conf.urls import patterns, url

from bikesurvey import views

urlpatterns = patterns('',
    # /bikesurvey/
    url(r'^$', views.AddSurveyInstanceView, name='index'),
    # /bikesurvey/list/
    url(r'^list/$', views.ListView, name='list'),
    # /bikesurvey/5/
    url(r'^(?P<surveyInstance_id>\d+)/$', views.AddBikerView, name='detail'),
    # /bikesurvey/thanks/
    url(r'^thanks/$', views.ThanksView, name='thanks'),
)
