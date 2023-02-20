from django.db import models

# Create your models here.
class student_field(models.Model):
    s_id = models.IntegerField(blank=False,null=False)
    name = models.TextField(max_length=25)
    rollno = models.IntegerField()
    age = models.IntegerField(help_text="your correct age")
    phone_no = models.IntegerField(null=True)
    DOB = models.IntegerField()
    summary = models.TextField(default="Good Student")
    height = models.DecimalField(null=True,blank=True,decimal_places=1, max_digits=3)


