from django.urls import path
from .views import AdvisorList, AdvisorDetails, StudentList, StudentDetails


urlpatterns = [
    path('advisors/', AdvisorList.as_view(), name='advisor-list'),
    path('advisors/<int:pk>/', AdvisorDetails.as_view(), name='advisor-detail'),
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>', StudentDetails.as_view(), name='student-detail'),
]