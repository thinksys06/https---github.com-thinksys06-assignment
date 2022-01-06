from rest_framework import serializers
from .models import class_detail
class CLASS_Serializer(serializers.ModelSerializer):
     class Meta:
          model = class_detail
          fields = ('__all__')