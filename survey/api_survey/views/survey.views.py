from django.shortcuts import render
from api_survey.models import Area
from api_survey.serializer import AreaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GetArea(APIView):
    def get(self, request, area_id):
        try:
            area = Area.objects.get(id=area_id)
        except Area.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AreaSerializer(area)
        return Response(serializer.data)