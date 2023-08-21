from django.urls import path
from rest_framework.views import APIView
from . import views
from .views import TypeProprieteApi,TypeProprieteApiDetails
from rest_framework.authtoken import views


urlpatterns = [
    path('login/',views.obtain_auth_token),
    path('viewset/propriete/', TypeProprieteApi.as_view()),
    path('viewset/propriete/<int:id>', TypeProprieteApiDetails.as_view()),
]