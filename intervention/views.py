from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rdv.models import  TypeIntervention
from rdv.serializer import TypeInterventionSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins 
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import datetime, random, string
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from datetime import date, datetime,time,timedelta
from django.db import transaction, IntegrityError
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class InterventionApi(APIView):

    pagination_class = PageNumberPagination
    queryset = TypeIntervention.objects.all()
    serializer_class = TypeInterventionSerializer
    paginator = pagination_class()

    def get(self,request):

        if request.GET.get("paginated",None) is not None:
            interventions = TypeIntervention.objects.all()
            serializer = TypeInterventionSerializer(interventions,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
            
        page = self.paginator.paginate_queryset(self.queryset,request,view=self)
        #if page is not None:
        serializer = self.serializer_class(page, many=True)
        return self.paginator.get_paginated_response(serializer.data)
        #interventions = TypeIntervention.objects.all()
        #serializer = TypeInterventionSerializer(interventions,many=True)
        #return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        with transaction.atomic():
            #création du Type d'intervention
            intervention = TypeIntervention.objects.create(
                type=data['type'],
                statut= int(data['statut']),
                created_at =  datetime.today()
            )
            intervention = TypeIntervention.objects.filter(pk=intervention.id)
            serializer = TypeInterventionSerializer(intervention,many=True)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    """@property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self,queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self,data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)"""


class InterventionApiDetails(APIView):

    def get(self,request,id):
        intervention = TypeIntervention.objects.filter(pk=id)
        if intervention.exists():
            serializer = TypeInterventionSerializer(intervention,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"status":"none"}, status=status.HTTP_204_NO_CONTENT)


    def put(self,request,id):
        data = request.data
        intervention = TypeIntervention.objects.filter(pk=id)
        if intervention.exists():
            intervention = intervention.first()
            
            with transaction.atomic():
                #edition Type inetrventio
                intervention.type=data['type']
                intervention.statut=data['statut']
                intervention.save()

                intervention = TypeIntervention.objects.filter(pk=id)
                serializer = TypeInterventionSerializer(intervention,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"status":"none"},status=status.HTTP_204_NO_CONTENT)

    def delete(self,request,id):
        intervention = TypeIntervention.objects.filter(pk=id)
        if intervention.exists():
            intervention.delete()
            return Response({"status":"done"},status=status.HTTP_200_OK)
        return Response({"status":"none"}, status=status.HTTP_204_NO_CONTENT)


