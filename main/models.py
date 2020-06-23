from django.db import models

# Create your models here.

class uploadFiles(models.Model):
    fname = models.CharField()
    up_date = models.DateTimeField(auto_now=True)
    fileL = models.FileField() 
