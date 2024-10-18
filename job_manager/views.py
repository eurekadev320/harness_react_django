from django.shortcuts import render
from job_manager.models import JobManager
from job_manager.serializer import JobManagerSerializer
from rest_framework import views
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter


class JobManagerView(views.APIView):

    def get(self,request):
        job_manager_obj=JobManager.objects.all()
        job_manager_serilaizer_obj=JobManagerSerializer(job_manager_obj,many=True)
        return Response(job_manager_serilaizer_obj.data)

    def post(self,request):
        serialize_obj=JobManagerSerializer(data=request.data)
        if serialize_obj.is_valid():
            serialize_obj.save()
            return Response(serialize_obj.data,status=status.HTTP_201_CREATED)
        return Response(serialize_obj.errors,status=status.HTTP_400_BAD_REQUEST)