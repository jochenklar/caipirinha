from django.db import models
from django.contrib.auth.models import User

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
    options = models.TextField(blank=True)
    required = models.BooleanField()

    def __unicode__(self):
        return self.name


class Detail(models.Model):
    user = models.ForeignKey(User, related_name='details')
    key = models.ForeignKey(DetailKey, unique=True, related_name='details')
    value = models.TextField(blank=True)

    def __unicode__(self):
        return '%s.%s' % (self.user.username,self.key)
