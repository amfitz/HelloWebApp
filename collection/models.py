from __future__ import unicode_literals

from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    slug = models.SlugField(unique=True)
