from django.db import models
class School(models.Model):
    student_name = models.CharField(max_length=200)
    student_rollnumber = models.IntegerField()
    student_class = models.IntegerField()

# Create your models here.
