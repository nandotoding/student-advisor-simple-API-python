from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

from .views import AdvisorList, AdvisorDetails, StudentList, StudentDetails, InvalidURLView

urlpatterns = [
    path('api/advisors/', AdvisorList.as_view(), name='advisor-list'),
    path('api/advisors/<str:pk>/', AdvisorDetails.as_view(), name='advisor-detail'),
    path('api/students/', StudentList.as_view(), name='student-list'),
    path('api/students/<str:pk>/', StudentDetails.as_view(), name='student-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', InvalidURLView.as_view()),
    path('<path:path>/', InvalidURLView.as_view()),
]
