from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from testapp.models import ProfileActivity,Profile
from testapp.serializers import ActivitySerializer,ProfileSerializer
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

from django.http import Http404
from rest_framework.views import APIView

@api_view(['GET', 'POST'])
def Profile_Activity(request):
    if request.method == 'GET':
        profile = Profile.objects.all()
        print(profile)
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)



