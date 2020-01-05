from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .. models import BlogPost

#converts to json
#allows for data validation , based on db constraints?
class BlogPostSerializer(serializers.ModelSerializer):
  url = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = BlogPost
    fields = [
      'url',
      'user',
      'title',
      'content',
      'timestamp'
    ]
    read_only_fields = ['url', 'user', 'timestamp', 'pk']

  def get_url(self, blogpost_obj):
    request = self.context.get('request')
    return blogpost_obj.get_api_url(request)

  #validating fields
  #title = serializers.CharField(max_length=120, validators=[UniqueValidator(queryset=BlogPost.objects.all())])

  def validate_title(self, value):
    try:
      qs = BlogPost.objects.get(title__iexact=value)
      if self.instance:
        qs.exclude(pk=self.instance.pk)
      if qs:
        raise serializers.ValidationError("The title must be unique")
      return value
    except BlogPost.DoesNotExist:  # no blogs exist so ofcourse value is valid
      return value
    except BlogPost.MultipleObjectsReturned:
      raise serializers.ValidationError("The title must be unique")
