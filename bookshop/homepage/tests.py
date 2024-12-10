import django.test
import http


class HomeTest(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = django.test.Client().get("/")
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
