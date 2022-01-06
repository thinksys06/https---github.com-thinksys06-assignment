from django.db import models
#from CLASS.models import class_details
class class_detail(models.Model):
    CLASS_name = models.IntegerField()
    CLASS_id = models.IntegerField()
    CLASS_teacher = models.CharField(max_length=200)

# Create your models here.

class School(models.Model):
    student_name = models.CharField(max_length=200)
    student_rollnumber = models.IntegerField()
    student_class = models.OneToOneField(class_detail, on_delete=models.CASCADE)
    #student_class=models.IntegerField()

# Create your models here.
