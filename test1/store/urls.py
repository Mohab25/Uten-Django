from django.urls import path,re_path
from .views import *

urlpatterns = [
    re_path(r'products/$',AllProducts.as_view(),name='all-products'),
    re_path(r'Latest/$',Latest.as_view(),name='latest-products'), 
    re_path(r'Latest/(?P<pk>\d+)/$',LatestProduct.as_view()), 
    re_path(r'Knife/$',Knife.as_view(),name='Knife-list'),
    re_path(r'Knife_Gallery/$',Knife_Gallery.as_view(),name='Knife-gallery'),
    re_path(r'Knife/(?P<pk>\d+)/$',Knife_product.as_view(),name='Knife-product'),
    re_path(r'Cup/$',Cup.as_view(),name='Cup-list'),
    re_path(r'Cup_Gallery/$',Cup_Gallery.as_view(),name='Cup-gallery'),
    re_path(r'Cup/(?P<pk>\d+)/$',Cup_product.as_view(),name='Cup-product'),
    re_path(r'Glass_Cup/$',Glass_Cup.as_view(),name='Glass_Cup-list'),
    re_path(r'Glass_Cup_Gallery/$',Glass_Cup_Gallery.as_view(),name='Glass_Cup-gallery'),
    re_path(r'Glass_Cup/(?P<pk>\d+)/$',Glass_Cup_product.as_view(),name='Glass_Cup-product'),
    re_path(r'Pan/$',Pan.as_view(),name='Pan-list'),
    re_path(r'Pan_Gallery/$',Pan_Gallery.as_view(),name='Pan-gallery'),
    re_path(r'Pan/(?P<pk>\d+)/$',Pan_product.as_view(),name='Pan-product'),
    re_path(r'Pot/$',Pot.as_view(),name='Pot-list'),
    re_path(r'Pot_Gallery/$',Pot_Gallery.as_view(),name='Pot-gallery'),
    re_path(r'Pot/(?P<pk>\d+)/$',Pot_product.as_view(),name='Pot-product'),
    re_path(r'Plate/$',Plate.as_view(),name='Plate-list'),
    re_path(r'Plate_Gallery/$',Plate_Gallery.as_view(),name='Plate-gallery'),
    re_path(r'Plate/(?P<pk>\d+)/$',Plate_product.as_view(),name='Plate-product'),
    re_path(r'Spoon/$',Spoon.as_view(),name='Spoon-list'),
    re_path(r'Spoon_Gallery/$',Spoon_Gallery.as_view(),name='Spoon-gallery'),
    re_path(r'Spoon/(?P<pk>\d+)/$',Spoon_product.as_view(),name='Spoon-product'),
    re_path(r'Collection/$',Collection.as_view(),name='Collection-list'),
    re_path(r'Collection_Gallery/$',Collection_Gallery.as_view(),name='Collection-gallery'),
    re_path(r'Collection/(?P<pk>\d+)/$',Collection_product.as_view(),name='Collection-product'),
    re_path(r'Cutting_board/$',Cutting_board.as_view(),name='Cutting_board-list'),
    re_path(r'Cutting_board_Gallery/$',Cutting_board_Gallery.as_view(),name='Cutting_board-gallery'),
    re_path(r'Cutting_board/(?P<pk>\d+)/$',Cutting_board_product.as_view(),name='Cutting_board-product'),
    re_path(r'Best/$',Best.as_view(),name='Best'),
    re_path(r'Best/(?P<pk>\d+)/$',BestProduct.as_view(),name='Best-Product'),


] 

