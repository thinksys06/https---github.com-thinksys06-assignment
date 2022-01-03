from django.db import models
from CLASS.models import class_detail
class School(models.Model):
    student_name = models.CharField(max_length=200)
    student_rollnumber = models.IntegerField()
    student_class = models.OneToOneField(class_detail, on_delete=models.CASCADE)
    #student_class=models.IntegerField()

# Create your models here.
