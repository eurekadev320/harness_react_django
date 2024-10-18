from django.contrib import admin
from .models import JobManager

admin.site.site_header = 'Admin | Job Manager'

admin.site.register(JobManager)


