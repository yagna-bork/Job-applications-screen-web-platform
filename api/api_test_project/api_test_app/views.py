from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from . serializers import EmployeeSerializer
import json

class EmployeeList(APIView):
  def get(self, req):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

  def post(self, req):
    json_string = req.body.decode('utf8').replace("'", '"')
    employeeJson = json.loads(json_string)
    employee = Employee(employeeJson['fName'], employeeJson['lName'])
    print("DEBUG: EmployeeList.post()\n" + str(employee))
    return Response()
