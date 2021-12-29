from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import CLASS_Serializer
from .models import class_detail
class CLASSViews(APIView):
    def post(self,request):
        serializer = CLASS_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id=None):
        if id:
            item= class_detail.objects.get(id=id)
            serializer= CLASS_Serializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items= class_detail.objects.all()
        serializer= CLASS_Serializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = class_detail.objects.get(id=id)
        serializer = CLASS_Serializer(item, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item= get_object_or_404(class_detail, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

# Create your views here.
