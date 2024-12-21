# views.py
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import Product
from .api_file.serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
def form_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        Product.objects.create(name=name, description=description, price=price)
        return redirect("/table")

    return render(request, 'form.html')


# def product_table(request):
#     products = Product.objects.all()
#     return render(request, 'table.html', {'products': products})


# def update(request, pk):
#     product = Product.objects.get(pk=pk)
#     if request.method == 'POST':
#         product.name = request.POST.get('name')
#         product.description = request.POST.get('description')
#         product.price = request.POST.get('price')
#         product.save()
#         return redirect('/table')

#     return render(request, 'update.html', {'product': product})


# def delete(request, pk):
#     product = Product.objects.get(pk=pk)
#     product.delete()
    
#     return redirect('/table',id)

# def home(request):
#     product=Product.objects.all()
    
#     data={
#         'product': list(product.values()) 
#     }

#     return JsonResponse(data)

# def detail(request,pk):
#     product=Product.objects.get(id=pk)

#     data={
#        'name': product.name,
#        'description':product.description,
#        'price':product.price,
#        'created_at':product.created_at
#     }
#     return JsonResponse(data)

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

