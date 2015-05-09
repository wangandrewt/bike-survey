from django.test import TestCase
from django.http import HttpRequest
from django.utils import timezone
from django.core.urlresolvers import reverse

from bikesurvey import views
from bikesurvey.models import SurveyInstance, Biker


class Helpers(object):

    @staticmethod
    def create_new_surveyInstance():
        s = SurveyInstance(name="A", location='Regents Drive @ Rt. 1')
        s.save()
        return s

    @staticmethod
    def create_new_biker(survey):
        b = Biker(surveyInstance=survey, bikerGender='M', bikerHelmet='N',
                  bikerLocation='Sidewalk')
        b.save()
        return b


class IndexViewTest(TestCase):

    def test_uses_correct_template(self):
        url = reverse('bikesurvey:index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'bikesurvey/welcome.html')
        self.assertEqual(response.status_code, 200)

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
        response = self.client.post(
            url, {'I_have_read_and_understand_the_instructions_above': '0'})
        self.assertTemplateUsed(response, 'bikesurvey/welcome.html')

        url = reverse('bikesurvey:index')
        response = self.client.post(
            url, {'I_have_read_and_understand_the_instructions_above': '1'})
        self.assertRedirects(response, reverse('bikesurvey:start'))


class ListViewTest(TestCase):

    def test_uses_correct_template(self):
        url = reverse('bikesurvey:list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'bikesurvey/list.html')
        self.assertEqual(response.status_code, 200)

    def test_one_biker(self):
        Helpers.create_new_biker(Helpers.create_new_surveyInstance())
        url = reverse('bikesurvey:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1 total', response.content)

    def test_zero_bikers(self):
        Biker.objects.all().delete()
        url = reverse('bikesurvey:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'0 total', response.content)

    def test_two_bikers(self):
        s = Helpers.create_new_surveyInstance()
        Helpers.create_new_biker(s)
        Helpers.create_new_biker(s)
        url = reverse('bikesurvey:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2 total', response.content)


class AddSurveyInstanceViewTest(TestCase):

    def test_uses_correct_template(self):
        url = reverse('bikesurvey:start')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'bikesurvey/create.html')
        self.assertEqual(response.status_code, 200)

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
        s = Helpers.create_new_surveyInstance()

        url = reverse('bikesurvey:detail', kwargs={'surveyInstance_id': s.id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'bikesurvey/detail.html')
        self.assertEqual(response.status_code, 200)

    def test_no_blank_biker_created(self):
        s = Helpers.create_new_surveyInstance()

        request = HttpRequest()
        request.method = 'GET'
        views.AddBikerView(request, s.id)
        self.assertEqual(Biker.objects.count(), 0)

        request = HttpRequest()
        request.method = 'POST'
        views.AddBikerView(request, s.id)
        self.assertEqual(Biker.objects.count(), 0)


class CommentsViewTest(TestCase):

    def test_uses_correct_template(self):
        s = Helpers.create_new_surveyInstance()

        url = reverse(
            'bikesurvey:comments', kwargs={'surveyInstance_id': s.id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'bikesurvey/comments.html')
        self.assertEqual(response.status_code, 200)


class ThanksViewTest(TestCase):

    def test_uses_correct_template(self):
        url = reverse('bikesurvey:thanks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'bikesurvey/thanks.html')
        self.assertEqual(response.status_code, 200)
