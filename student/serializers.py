from rest_framework import serializers
from .models import School
class SchoolSerializer(serializers.ModelSerializer):
     student_name = serializers.CharField(max_length=200)
     student_rollnumber = serializers.IntegerField()
     student_class = serializers.IntegerField()
    
class Meta:
        model = School
        fields = ('_all_')