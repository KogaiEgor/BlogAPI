from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Blog(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.PROTECT)
    record = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True,
                                max_length=1024,
                                upload_to='blog/media')
    profile_pic = models.URLField(null=True)

