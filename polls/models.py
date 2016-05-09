from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices")
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    text = models.CharField(max_length=25)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text