from django import views
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rdv.models import  TypePropriete
from rdv.serializer import TypeProprieteSerializer
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

class TypeProprieteApi(APIView):

    pagination_class=PageNumberPagination
    serializer_class= TypeProprieteSerializer
    queryset = TypePropriete.objects.all()
    paginator = pagination_class()

    def get(self,request):
        if request.GET.get("paginated",None) is not None:
            propriete = TypePropriete.objects.all()
            serializer = TypeProprieteSerializer(propriete,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
            
        page = self.paginator.paginate_queryset(self.queryset,request,view=self)
        #if page is not None:
        serializer = self.serializer_class(page, many=True)
        return self.paginator.get_paginated_response(serializer.data)
       #propriete = TypePropriete.objects.all()
        #serializer = TypeProprieteSerializer(propriete,many=True)
        #return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        with transaction.atomic():
            #création du Type de propriété
            propriete =TypePropriete.objects.create(
                type=data['type'],
                statut= int(data['statut']),
                created_at =  datetime.today()
            )
            propriete = TypePropriete.objects.filter(pk=propriete.id)
            serializer = TypeProprieteSerializer(propriete,many=True)
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

class TypeProprieteApiDetails(APIView):

    def get(self,request,id):
        propriete = TypePropriete.objects.filter(pk=id)
        if propriete.exists():
            serializer = TypeProprieteSerializer(propriete,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"status":"none"}, status=status.HTTP_204_NO_CONTENT)


    def put(self,request,id):
        data = request.data
        propriete = TypePropriete.objects.filter(pk=id)
        if propriete.exists():
            propriete = propriete.first()
            
            with transaction.atomic():
                #edition Type inetrventio
                propriete.type=data['type']
                propriete.statut=data['statut']
                propriete.save()

                propriete = TypePropriete.objects.filter(pk=id)
                serializer = TypeProprieteSerializer(propriete,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"status":"none"},status=status.HTTP_204_NO_CONTENT)

    def delete(self,request,id):
        propriete = TypePropriete.objects.filter(pk=id)
        if propriete.exists():
            propriete.delete()
            return Response({"status":"done"},status=status.HTTP_200_OK)
        return Response({"status":"none"}, status=status.HTTP_204_NO_CONTENT)


