# views.py
from django.shortcuts import render, redirect
from .models import Product,Showroom
from .api_file.serializer import ProductSerializer,ShowroomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny,IsAdminUser

class showroom_view(APIView):
    # authentication_classes=[SessionAuthentication]
    # authentication_classes=[BasicAuthentication]

    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]

    def get(self,request):
        showroom=Showroom.objects.all()
        serializer=ShowroomSerializer(showroom, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class showroom_detail(APIView):
    def get(self,request,pk):
        showroom=Showroom.objects.get(pk=pk)
        serializer=ShowroomSerializer(showroom)
        return Response(serializer.data)
    
    def put(self,request,pk):
        showroom=Showroom.objects.get(pk=pk)
        serializer=ShowroomSerializer(showroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("invali data")
    def delete(self,request,pk):
        showroom=Showroom.objects.get(pk=pk)
        showroom.delete()
        return Response("the data is delete successfully")




@csrf_exempt
@api_view(['GET','POST'])
def home(request):
    if request.method=='GET':
        product=Product.objects.all()
        serializer=ProductSerializer(product, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def detail(request,pk):
    if request.method=="GET":
        product=Product.objects.get(id=pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    if request.method=="PUT":
        product=Product.objects.get(id=pk)
        serializer=ProductSerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)
    
    if request.method=="DELETE":
        product=Product.objects.get(id=pk)
        return Response("Product is delete")

