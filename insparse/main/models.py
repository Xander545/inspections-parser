from django.db import models

# Create your models here.

class InspectionSource(models.Model):
    url = models.CharField(max_length=200)
    code = models.CharField(max_length=50, default="default")
    department_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.department_name    


class InspectionLoadHistory(models.Model):
    source = models.ForeignKey(InspectionSource, on_delete=models.CASCADE)
    load_date = models.DateTimeField('Loading datetime')
    count_rows = models.IntegerField('Count rows of loading')

    def __str__(self):
        return "{} - {}".format(self.load_date, self.source)


class Company(models.Model):
    inn = models.CharField(max_length=10, help_text='ИНН')
    company_name = models.CharField(max_length=200)
    head_of_company = models.CharField(max_length=200, blank=True, null=True)
    phones = models.CharField(max_length=200, blank=True, null=True)
    mail = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_in_law = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.company_name


class Region(models.Model):
    region_name = models.CharField(max_length=200)

    def __str__(self):
        return self.region_name


class InspectionType(models.Model):
    inspection_type = models.CharField(max_length=200)

    def __str__(self):
        return self.inspection_type


class InspectionStatus(models.Model):
    status_name = models.CharField(max_length=200)

    def __str__(self):
        return self.status_name    


class Inspection(models.Model):
    inspection_date = models.DateField('Date of inspecting', blank=True, null=True)
    source = models.ForeignKey(InspectionSource, on_delete=models.CASCADE, default=-1)
    inspection_place = models.CharField(max_length=500, default="no place")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=-1)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=-1)
    type = models.ForeignKey(InspectionType, on_delete=models.CASCADE, default=-1)
    status = models.ForeignKey(InspectionStatus, on_delete=models.CASCADE, default=-1)
    comment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.company.company_name