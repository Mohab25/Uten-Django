from rest_framework import serializers 
from .models import *

class PanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields=('__all__')

class FirstBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstBanner
        fields=('__all__')

class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields=('__all__')
    
class SecondBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondBanner
        fields=('__all__')

class ContactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields=('__all__')

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields=('__all__')

