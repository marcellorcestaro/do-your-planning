""" Views para planilha de gastos """

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Fixo
from .serializers import FixoSerializer
from rest_framework import generics
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello')

class FixosList(generics.ListCreateAPIView):
    queryset = Fixo.objects.all()
    serializer_class = FixoSerializer
