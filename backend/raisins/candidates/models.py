from django.db import models
from django.contrib import admin
from raisins.jobs.models import Job


class Candidate(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    middlename = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=64, null=True, blank=True)
    jobs = models.ManyToManyField(Job)
    address = models.CharField(max_length=255, null=True, blank=True)
    salary_expectation = models.DecimalField(max_digits=32, decimal_places=2, null=True, blank=True)
    timezone = models.CharField(max_length=16, null=True, blank=True)
    resume = models.BinaryField(null=True, blank=True)
    cover_letter = models.BinaryField(null=True, blank=True)


class CandidateJobStep(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='steps')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    step = models.PositiveSmallIntegerField(default=0)



admin.site.register(Candidate)
admin.site.register(CandidateJobStep)
