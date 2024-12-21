from django.db import models

# Create your models here.
class Job(models.Model):
    job_title= models.CharField(max_length=255)
    company= models.CharField(max_length=255)
    location= models.CharField(max_length=255)
    posted_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    location_type=models.CharField(max_length=40)
    compensation=models.CharField(max_length=50)
    employment_type=models.CharField(max_length=50)
    skills=models.TextField()
    job_details=models.TextField()

    def __str__(self):
        return self.job_title



