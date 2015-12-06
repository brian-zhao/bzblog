from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    author = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})
