from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

class JobAPITestCase(APITestCase):
  def test_valid_all_jobs_call(self):
    url = api_reverse('api-jobs:get-all-jobs')
    response = self.client.get(url, {}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_valid_all_available_jobs_call(self):
    url = api_reverse('api-jobs:get-all-available-jobs')
    response = self.client.get(url, {}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)


