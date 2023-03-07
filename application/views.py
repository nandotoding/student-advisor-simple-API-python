from rest_framework import generics
from .models import Advisor, Student
from .serializers import AdvisorSerializer, StudentSerializer


class AdvisorList(generics.ListCreateAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer


class AdvisorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
