import django.test
import http

class CatalogTest(django.test.TestCase):
    def test_static_catalog_endpoint(self):
        response = django.test.Client().get('/catalog/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

# class ItemListTest(django.test.TestCase):
