from django.test import TestCase
from django.urls import reverse


class TestPage(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("main:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/home.html")
        self.assertContains(response, "home page")

    def test_about_page(self):
        response = self.client.get(reverse("main:about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/about.html")
        self.assertContains(response, "about page")
