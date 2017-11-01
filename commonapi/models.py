from django.db import models

# Create your models here.

class t_stburls(models.Model):
    pkid=models.AutoField(primary_key=True)
    stbnum=models.CharField(max_length=64)
    url=models.CharField(max_length=256)