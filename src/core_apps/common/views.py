from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK


class HealthCheck(APIView):
    "API for Healthcheck of Algocode Auth Service."

    def get(self, request, format=None):
        """Healthcheck for Algocode Auth Service"""
        return Response({"status": "OK"}, HTTP_200_OK)
