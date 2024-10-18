from django.db import models


class JobManager(models.Model):
    job_title=models.CharField(max_length=250)
    skills=models.CharField(max_length=250)
    description=models.CharField(max_length=500)
    created_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_title

