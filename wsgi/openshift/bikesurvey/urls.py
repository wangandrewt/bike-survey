from django.conf.urls import patterns, url

from bikesurvey import views

urlpatterns = patterns('',
    # /
    url(r'^$', views.IndexView, name='index'),
    # start/
    url(r'^start/$', views.AddSurveyInstanceView, name='start'),
    # list/
    url(r'^list/$', views.ListView, name='list'),
    # 5/
    url(r'^(?P<surveyInstance_id>\d+)/$', views.AddBikerView, name='detail'),
    # thanks/
    url(r'^thanks/$', views.ThanksView, name='thanks'),
)
