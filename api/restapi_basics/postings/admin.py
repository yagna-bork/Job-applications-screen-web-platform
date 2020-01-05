from django.contrib import admin

from . models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(BlogPost, BlogPostAdmin)
