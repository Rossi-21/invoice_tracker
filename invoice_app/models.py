from django.db import models
from django.contrib.auth.models import User


class Invoice(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    vendor = models.ForeignKey(
        'Vendor', on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE, null=True, blank=True)
    total = models.FloatField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vendor} - Total: {self.total}'


class Vendor(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Department(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()

    def __str__(self):
        return str(self.name)
