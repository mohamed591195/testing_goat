from django.test import TestCase


class SmokeTest(TestCase):


    
    def test_template_used_for_home(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')
    
    def test_can_save_a_post_request(self):
        response = self.client.post('/', data={'item_text': 'reading more about TDD in django'})
        self.assertIn('reading more about TDD in django', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')
