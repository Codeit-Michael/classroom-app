from django.shortcuts import render
from django.http import HttpResponse

from .serializers import studentSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student

# Create your views here.
@api_view(['GET'])
def first(response):
	st = student.objects.all()
	srl = studentSerializer(st,many=True)
	return Response(srl.data)

# not working
# class first(APIView):
# 	def get(self,request,format=None):
# 		queryset = student.objects.all()
# 		serializer = studentSerializer(student,many=True)
# 		return Response(serializer.data)