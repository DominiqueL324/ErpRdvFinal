from django.urls import path
from rest_framework.views import APIView
from . import views
from .views import RDVApi,RdvApiFiltres
from rest_framework.authtoken import views


urlpatterns = [
    path('viewset/tri/', RDVApi.as_view()),
    path('viewset/filtre/', RdvApiFiltres.as_view()),
]
