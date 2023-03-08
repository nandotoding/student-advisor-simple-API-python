from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import AdvisorList, AdvisorDetails, StudentList, StudentDetails


urlpatterns = [
    path('advisors/', AdvisorList.as_view(), name='advisor-list'),
    path('advisors/<int:pk>/', AdvisorDetails.as_view(), name='advisor-detail'),
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>', StudentDetails.as_view(), name='student-detail'),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
]