from rest_framework import serializers
from .models import class_detail
class CLASS_Serializer(serializers.ModelSerializer):
     CLASS_name = serializers.IntegerField()
     CLASS_ID = serializers.IntegerField()
     CLASS_teacher = serializers.CharField(max_length=200)
    
class Meta:
        model = class_detail
        fields = ('_all_')