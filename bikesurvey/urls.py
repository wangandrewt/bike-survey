from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from bikesurvey import views


urlpatterns = patterns("",
                       url(r'^favicon.ico$',
                           RedirectView.as_view(
                               url=staticfiles_storage.url('favicon.ico'),
                               permanent=False),
                           name='favicon'),
                       url(r'^humans.txt$',
                           RedirectView.as_view(
                               url=staticfiles_storage.url('humans.txt'),
                               permanent=False),
                           name='humanstxt'),
                       # /
                       url(r'^$', views.IndexView, name='index'),
                       # start/
                       url(r'^start/$', views.AddSurveyInstanceView,
                           name='start'),
                       # list/
                       url(r'^list/$', views.ListView, name='list'),
                       # 5/
                       url(r'^(?P<surveyInstance_id>\d+)/$',
                           views.AddBikerView, name='detail'),
                       # 5/comments/
                       url(r'^(?P<surveyInstance_id>\d+)/comments/$',
                           views.CommentsView, name='comments'),
                       # thanks/
                       url(r'^thanks/$', views.ThanksView, name='thanks'),
                       )
