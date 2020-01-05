from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

class LoginAPITestCase(APITestCase):
  def test_login_valid_detail_test(self):
    url = api_reverse('api-auth:normal-login')
    response = self.client.post(url, data={"email": "test_user_one@gmail.com", "password": "hashed_password_one"}, format='json')
    print(response)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_login_admin_valid_details_test(self):
    url = api_reverse('api-auth:admin-login')
    response = self.client.post(url, data={"email": "admin_test_one@gmail.com", "password": "admin_password_one"}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
