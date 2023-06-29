from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Applicants
from .forms import ApplicantForm

from django.test import TestCase, Client
from django.urls import reverse
from .forms import ApplicantForm

class CreateApplicationViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_application_post_success(self):
        # Prepare test data
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'address' :'Lagos',
            'phone_number':'555-333-344',
            'resume_link':'www.google.com',
            'role':'BACKEND DEVELOPER',
            
        }
        response = self.client.post(reverse('create_application'), data)
        #self.assertEqual(response.status_code, 302)
        #self.assertRedirects(response, reverse('application_success'))
        self.assertTrue(Applicants.objects.filter(first_name='John', last_name='Doe').exists())


    def test_create_application_get(self):
        response = self.client.get(reverse('create_application'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'applications/create_application.html')
        self.assertIsInstance(response.context['application_form'], ApplicantForm)
