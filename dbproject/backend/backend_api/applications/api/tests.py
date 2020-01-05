from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

# class ApplicationAPITestCase(APITestCase):
#   def test_get_feedback_valid(self):
#     url = api_reverse('api-applications:get-feedback-for-user')
#     data = {"invalid_key", "asdasd"}
#     response = self.client.get(url, data, format='json')
#     self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
