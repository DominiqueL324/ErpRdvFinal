from django.urls import path
from rest_framework.views import APIView
from . import views
from .views import InterventionApi,InterventionApiDetails
from rest_framework.authtoken import views


urlpatterns = [
    path('login/',views.obtain_auth_token),
    path('viewset/intervention/', InterventionApi.as_view()),
    path('viewset/intervention/<int:id>', InterventionApiDetails.as_view()),
]