from django.shortcuts import render

from .serializers import HelloSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


# 2 ways of writing the Apis
	# Functiona Based Apis
	# class Based Apis

# HTTPs Methods:-
	# GET -- for getting single or multiple people details
	# POST -- for sending the new data.
	# PUT -- for updating the already existed data.
	# DELETE -- for deleting the details..


# Serializers -- same as forms.py in normal django


# Function Based:
@api_view(['GET','POST'])
def hello_api(request):
	if request.method=="POST":
		ser = HelloSerializer(data=request.data)
		if ser.is_valid():
			return Response(ser.data)
		else:
			return Response({'message':"Validition Missing"})
	else:
		return Response({"message":"Method Not Allowed"})