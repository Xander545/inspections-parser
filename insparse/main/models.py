from django.db import models

# Create your models here.

class InspectionSource(models.Model):
    url = models.CharField(max_length=200)
    department_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class InspectionLoadHistory(models.Model):
    source = models.ForeignKey(InspectionSource, on_delete=models.CASCADE)
    load_date = models.DateTimeField('Loading datetime')
    count_rows = models.IntegerField('Count rows of loading')


class Company(models.Model):
    inn = models.IntegerField('Count rows of loading')
    company_name = models.CharField(max_length=200)
    head_of_company = models.CharField(max_length=200)
    phones = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address_in_law = models.CharField(max_length=200)


class Region(models.Model):
    region_name = models.CharField(max_length=200)


class InspectionType(models.Model):
    inspection_type = models.CharField(max_length=200)


class InspectionStatus(models.Model):
    status_name = models.CharField(max_length=200)    


class Inspection(models.Model):
    insection_date = models.DateTimeField('Date of inspecting', blank=True, null=True)
    source = models.ForeignKey(InspectionSource, on_delete=models.CASCADE, default=-1)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=-1)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=-1)
    type = models.ForeignKey(InspectionType, on_delete=models.CASCADE, default=-1)
    status = models.ForeignKey(InspectionStatus, on_delete=models.CASCADE, default=-1)
    comment = models.CharField(max_length=200, blank=True, null=True)
