from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = self.client.get('/')
        self.assertContains(response, '<title>To-Do</title>')
        self.assertContains(response, '<html>')
        self.assertContains(response, '</html>')
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={"item_text": "A new list item"})
        self.assertContains(response, "A new list item")
        self.assertTemplateUsed(response, 'home.html')
