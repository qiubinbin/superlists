from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        reponse = home_page(request)
        self.assertTrue(reponse.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', reponse.content)
        self.assertTrue(reponse.content.endswith(b'</html>'))
