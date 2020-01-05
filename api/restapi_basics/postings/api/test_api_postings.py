from rest_framework.test import APITestCase
from ..models import BlogPost
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogPostAPITestCase(APITestCase):
  def setUp(self):
    user_obj = User(username='testcfeuser', email='test@test.mail')
    user_obj.set_password('password')
    user_obj.save()
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



