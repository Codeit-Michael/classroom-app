# required
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from .models import student
from .serializers import studentSerializer

# for function based views
from rest_framework.decorators import api_view

# for class based views
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def students(request):
	st = student.objects.all()
	srl = studentSerializer(st,many=True)
	return Response(srl.data)

@api_view(['GET'])
def view_student(request,id):
	st = student.objects.get(id=id)
	srl = studentSerializer(st,many=False)
	return Response(srl.data)

@api_view(['POST'])
def add_student(request,id):
	srl = studentSerializer(data=request.data)
	if srl.is_valid():
		srl.save()
	return Response(srl.data)

@api_view(['DELETE'])
def remove_student(request,id):
	st = student.objects.get(id=id)
	st.delete()
	return Response('Student Removed')

@api_view(['POST'])
def update_student(request,id):
	st = student.objects.get(id=id)
	srl = studentSerializer(instance=st,data=request.data)
	if srl.is_valid():
		srl.save()
	return Response(srl.data)

# class based views
# class first(APIView):
# 	def get(self,request):
# 		sets = student.objects.all()
# 		serializer = studentSerializer(sets,many=True)
# 		return Response(serializer.data)

# 	def post(self,request):
# 		serializer = studentSerializer(data = request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
