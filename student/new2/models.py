from django.db import models

# Create your models here.

class student(models.Model):
    f_id = models.IntegerField()
    s_fee = models.IntegerField()
    fee_status = models.TextField()
    
