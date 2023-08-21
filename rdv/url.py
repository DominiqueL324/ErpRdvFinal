from django.urls import path
from rest_framework.views import APIView
from . import views
from .views import RDVApi,RDVApiDetails,RDVReportedAgentApi,RDVReportedApi
from rest_framework.authtoken import views


urlpatterns = [
    path('login/',views.obtain_auth_token),
    path('viewset/rdv/', RDVApi.as_view()),
    path('viewset/rdv/<int:id>', RDVApiDetails.as_view()),
    path('viewset/updated/agent', RDVReportedAgentApi.as_view()),
    path('viewset/updated/date', RDVReportedApi.as_view()),
]