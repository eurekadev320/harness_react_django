'''
Author : Manikandan Kasi
'''

from rest_framework import serializers
from .models import JobManager

class JobManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobManager
        fields='__all__'
