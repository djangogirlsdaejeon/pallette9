from django.db import models
from django.utils import timezone

class Photo(models.Model):
    author = models.ForeignKey('auth.User')
    contents = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(auto_now=True)
    pic = models.ImageField()
    color_tag = models.CharField(max_length=6, default="")

    class Meta:
        ordering = ['-created_date']

