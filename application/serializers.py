from rest_framework import serializers
from .models import Advisor, Student


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    advisor = AdvisorSerializer()

    class Meta:
        model = Student
        fields = '__all__'
