'''
Author : Manikandan Kasi
'''

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('createJob/',views.JobManagerView.as_view()),
    path('distinct/skills/',views.JobManagerView.as_view()),
]

