from django.shortcuts import render
from .models import * 
from .serializers import *
from rest_framework import generics 

class PanelView(generics.ListCreateAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer

class PanelEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer

class FirstBannerView(generics.ListCreateAPIView):
    queryset = FirstBanner.objects.all()
    serializer_class = FirstBannerSerializer

class FirstBannerEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FirstBanner.objects.all()
    serializer_class = FirstBannerSerializer

class GalleryItemView(generics.ListCreateAPIView):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer

class GalleryItemEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer

class SecondBannerView(generics.ListCreateAPIView):
    queryset = SecondBanner.objects.all()
    serializer_class =  SecondBannerSerializer

class SecondBannerEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SecondBanner.objects.all()
    serializer_class = SecondBannerSerializer

class ContactSectionView(generics.ListCreateAPIView):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSectionSerializer

class ContactSectionEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSectionSerializer

class FooterView(generics.ListCreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

class FooterEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
