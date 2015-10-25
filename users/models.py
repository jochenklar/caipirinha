from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField


class DetailKey(models.Model):

    TYPE_CHOICES = (
        ('text', 'Input field'),
        ('textarea', 'Textarea field'),
        ('checkbox', 'Checkbox'),
        ('radio', 'Radio button'),
        ('select', 'Select field'),
        ('multiselect', 'Multiselect field'),
    )

    name = models.SlugField()
    type = models.CharField(max_length=8,choices=TYPE_CHOICES)
    hint = models.TextField(blank=True)
    options = JSONField()
    required = models.BooleanField()

    def __unicode__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='details')
    details = JSONField()

    def __unicode__(self):
        return '%s' % self.user.username
