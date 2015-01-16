from django.test import TestCase
from django.http import HttpRequest
from django.utils import timezone
from django.core.urlresolvers import reverse

from bikesurvey import views
from bikesurvey.models import SurveyInstance, Biker


class IndexViewTest(TestCase):

    def test_uses_correct_template(self):
        url = reverse('bikesurvey:index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'bikesurvey/welcome.html')
        
    def test_must_agree_to_continue(self):
        request = HttpRequest()
        request.method = 'GET'
        response = views.IndexView(request)
        self.assertTemplateUsed(response, 'bikesurvey/welcome.html')
        
        request = HttpRequest()
        request.method = 'POST'
        response = views.IndexView(request)
        self.assertTemplateUsed(response, 'bikesurvey/welcome.html')
        
        url = reverse('bikesurvey:index')
        response = self.client.post(url, {'I_have_read_and_understand_the_instructions_above': '0'})
        self.assertTemplateUsed(response, 'bikesurvey/welcome.html')
        
        url = reverse('bikesurvey:index')
        response = self.client.post(url, {'I_have_read_and_understand_the_instructions_above': '1'})
        self.assertRedirects(response, reverse('bikesurvey:start'))


class AddSurveyInstanceViewTest(TestCase):
    
    def test_uses_correct_template(self):
        url = reverse('bikesurvey:start')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'bikesurvey/create.html')
    
    def test_no_blank_surveyInstance_created(self):
        request = HttpRequest()
        request.method = 'GET'
        views.AddSurveyInstanceView(request)
        self.assertEqual(SurveyInstance.objects.count(), 0)
        
        request = HttpRequest()
        request.method = 'POST'
        views.AddSurveyInstanceView(request)
        self.assertEqual(SurveyInstance.objects.count(), 0)


class AddBikerViewTest(TestCase):
    
    def test_uses_correct_template(self):
        # Create new SurveyInstance
        s = SurveyInstance(date=timezone.now(), name="A", location='Regents Drive @ Rt. 1')
        s.save()
        
        url = reverse('bikesurvey:detail', kwargs={'surveyInstance_id': s.id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'bikesurvey/detail.html')
    
    def test_no_blank_biker_created(self):
        # Create new SurveyInstance
        s = SurveyInstance(date=timezone.now(), name="A", location='Regents Drive @ Rt. 1')
        s.save()
        
        request = HttpRequest()
        request.method = 'GET'
        views.AddBikerView(request, s.id)
        self.assertEqual(Biker.objects.count(), 0)
        
        request = HttpRequest()
        request.method = 'POST'
        views.AddBikerView(request, s.id)
        self.assertEqual(Biker.objects.count(), 0)


class ThanksViewTest(TestCase):

    def test_uses_correct_template(self):
        url = reverse('bikesurvey:thanks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'bikesurvey/thanks.html')

