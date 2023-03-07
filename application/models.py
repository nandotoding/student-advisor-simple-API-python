from django.db import models


class Advisor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
