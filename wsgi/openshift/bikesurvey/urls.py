from django.conf.urls import patterns, url

from bikesurvey import views

urlpatterns = patterns('',
    # ex: /bikesurvey/
    url(r'^$', views.index, name='index'),
    # ex: /bikesurvey/5/
    url(r'^(?P<surveyInstance_id>\d+)/$', views.detail, name='detail'),
    # ex: /bikesurvey/5/record/
    url(r'^(?P<surveyInstance_id>\d+)/record/$', views.record, name='record'),
)
