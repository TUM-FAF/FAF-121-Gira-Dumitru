from django.db import models
from django.db.models import permalink

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()



    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'title': self.title })

