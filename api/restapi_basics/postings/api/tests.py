from rest_framework.test import APITestCase
from ..models import BlogPost
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER


User = get_user_model()

class BlogPostAPITestCase(APITestCase):
  def setUp(self):
    user_obj = User.objects.create(
      username='testcfeuser', 
      email='test@test.mail', 
      password='password')
    BlogPost.objects.create(
      user=user_obj,
      title='test_blog', 
      content='test_blog_content')

  def test_single_user(self):
    user_count = User.objects.count()
    self.assertEqual(user_count, 1)
  
  def test_single_blogpost(self):
    blogpost_count = BlogPost.objects.count()
    self.assertEqual(blogpost_count, 1)

  def test_get_list(self):
    url = api_reverse('api-postings:post-list') #how does relative url work?
    response = self.client.get(url, {}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_put_item_unauthorised(self):
    data = {"title" : "automated test article", "content" : "random content"}
    url = api_reverse('api-postings:post-list')
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_get_item(self):
    data = {}
    url = BlogPost.objects.first().get_api_url()
    response = self.client.get(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_update_existing_item_unauthorised(self):
    data = {'title': 'something', 'content': 'unauthorised'}
    url = BlogPost.objects.first().get_api_url()
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_post_existing_item_unauthorised(self):
    data = {'title': 'something', 'content': 'unauthorised'}
    url = BlogPost.objects.first().get_api_url()
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

  def test_update_existing_item_authorised(self):
    #jwt authorization
    user = User.objects.first()
    payload = payload_handler(user)
    token_response = encode_handler(payload)
    self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)
    
    data = {'title': 'updated title', 'content': 'updated content authorized'}
    url = BlogPost.objects.first().get_api_url()
    # print("DEBUG: test_update_existing_item_authorised(): " + BlogPost.objects.first().title)
    
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    # print("DEBUG: test_update_existing_item_authorised(): " + str(response.data))
  
  def test_post_blog_authorised(self):
    #authenticate current user
    user = User.objects.first()
    payload = payload_handler(user)
    token_response = encode_handler(payload)
    self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)

    #build request
    data = {'title': 'newly created test blog', 'content': 'newly created test blog authorised'}
    url = api_reverse('api-postings:post-list')
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_put_blog_not_owner_but_authorized(self):
    new_user = User.objects.create(
      username='sometestuser', 
      password='sometestuser'
    )
    new_blogpost = BlogPost.objects.create(
      user=new_user,
      title='blog by sometestuser',
      content='blog by sometestuser'
    )
    
    #authenticate diff user to above
    user = User.objects.first()
    payload = payload_handler(user)
    token_response = encode_handler(payload)
    self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)

    self.assertNotEqual(new_user.username, user.username)

    #attempted put request
    data = {
      'title': 'blog post edited by testcfeuser',
      'content': 'content edited by testcfeuser from sometestuser'
    }
    url = new_blogpost.get_api_url()
    response = self.client.put(url, data, format='json')

    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
  
  #this test fails but fine for now
  def test_get_token_and_update_valid_post(self):
    #getting jwt token for default user
    user = User.objects.first()
    data = {
        'username': user.username,
        'password': user.password
    }
    url = api_reverse('api-login')
    response = self.client.post(url, data, format='json')
    # self.assertEqual(response.status_code, status.HTTP_200_OK)

    print("DEBUG test_get_token_and_update_valid_post(). Token: {0}\n Url: {1} \nData: {2} \nuser.isActive: {3}".format(
        response.data, url, data, user.is_active))

    #using token to make update request to existing owned blog
    # self.client.credentials(HTTP_AUTHORIZATION='JWT ' + )
    new_blog = {
      'title': 'updating using jwt token from api',
      'content': 'updating using jwt token from api'
    }
    url = BlogPost.objects.first().get_api_url()
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
