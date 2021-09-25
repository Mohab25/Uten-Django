from django.shortcuts import render
from .models import Product
from rest_framework import generics 
from .serializers import ProductSerializer

class AllProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Latest(generics.ListCreateAPIView):
    queryset = Product.objects.filter(feature__icontains='Latest')[:6]
    serializer_class = ProductSerializer

class LatestProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(feature__icontains='Latest')
    serializer_class = ProductSerializer


class Best(generics.ListCreateAPIView):
    queryset = Product.objects.filter(feature__icontains='Best')[:6]
    serializer_class = ProductSerializer

class BestProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(feature__icontains='Best')
    serializer_class = ProductSerializer


# pages for each product type (Knife,Spoon,Pot, .. ), and according
# to the type, the filter will take place.. 

class Knife(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Knife')
    serializer_class = ProductSerializer

class Knife_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Knife_Gallery(generics.ListCreateAPIView):
    # this is limited by 7 items specifically for the gallery items
    queryset = Product.objects.filter(product_type__iexact='Knife')[:7]
    serializer_class = ProductSerializer


class Cup(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Cup')
    serializer_class = ProductSerializer

class Cup_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Cup_Gallery(generics.ListCreateAPIView):
    # this is limited specifically for the gallery items 
    queryset = Product.objects.filter(product_type__iexact='Cup')[:7]
    serializer_class = ProductSerializer


class Glass_Cup(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Glass Cup')
    serializer_class = ProductSerializer

class Glass_Cup_Gallery(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Glass Cup')[:7]
    serializer_class = ProductSerializer

class Glass_Cup_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Pan(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Pan')
    serializer_class = ProductSerializer

class Pan_Gallery(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Pan')[:7]
    serializer_class = ProductSerializer

class Pan_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Pot(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Pot')
    serializer_class = ProductSerializer

class Pot_Gallery(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Pot')[:7]
    serializer_class = ProductSerializer

class Pot_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Plate(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Plate')
    serializer_class = ProductSerializer

class Plate_Gallery(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Plate')[:7]
    serializer_class = ProductSerializer

class Plate_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Spoon(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Spoon')
    serializer_class = ProductSerializer

class Spoon_Gallery(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Spoon')[:7]
    serializer_class = ProductSerializer

class Spoon_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Collection(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Collection')
    serializer_class = ProductSerializer

class Collection_Gallery(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Collection')[:7]
    serializer_class = ProductSerializer

class Collection_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Cutting_board(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Cutting board')
    serializer_class = ProductSerializer

class Cutting_board_Gallery(generics.ListCreateAPIView):
    queryset = Product.objects.filter(product_type__iexact='Cutting board')[:7]
    serializer_class = ProductSerializer

class Cutting_board_product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




