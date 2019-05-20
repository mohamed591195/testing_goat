from django.test import TestCase


class SmokeTest(TestCase):


    
    def test_template_used_for_home(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')
