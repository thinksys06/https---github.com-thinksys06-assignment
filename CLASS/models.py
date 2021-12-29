from django.db import models
class class_detail(models.Model):
    CLASS_name = models.IntegerField()
    CLASS_id = models.IntegerField()
    CLASS_teacher = models.CharField(max_length=200)

# Create your models here.
