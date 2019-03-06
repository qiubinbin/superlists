from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        reponse = home_page(request)
        # expected_html = render_to_string('home.html')
        self.assertTrue(reponse.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', reponse.content)
        self.assertTrue(reponse.content.endswith(b'</html>'))
        # self.assertEqual(reponse.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        expect_html=render_to_string(
            'home.html',
            {'new_item_text':'A new list item'}
        )
        self.assertEqual(response.content.decode(),expect_html)
