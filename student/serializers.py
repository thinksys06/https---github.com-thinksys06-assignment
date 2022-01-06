from rest_framework import serializers
from .models import School
#from CLASS.models import class_detail
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
          model = School
          fields = ('__all__')