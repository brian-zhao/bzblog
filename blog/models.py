from django.db import models
from django.db.models import permalink


class Blog(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})


class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})
