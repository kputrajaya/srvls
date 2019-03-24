from django.test import TestCase
from django.urls import reverse


class ViewTests(TestCase):
    def test_get_log(self):
        res = self.client.get(reverse('master:logs'))
        self.assertEqual(res.status_code, 200)

    def test_post_log(self):
        data = {'foo': 'bar'}
        res = self.client.post(reverse('master:logs'), data, content_type='application/json')
        self.assertEqual(res.status_code, 400)

        data = {'message': 'Lorem ipsum dolor sit amet'}
        res = self.client.post(reverse('master:logs'), data, content_type='application/json')
        self.assertEqual(res.status_code, 201)

        res = self.client.get(reverse('master:logs'))
        self.assertIn(data['message'], str(res.content))
