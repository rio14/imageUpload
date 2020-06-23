from django.db import models

# Create your models here.

class uploadFiles(models.Model):
    fname = models.CharField(max_length=None)
    up_date = models.DateTimeField(auto_now=True)
    fileL = models.FileField() 
