from django.urls import re_path,path
from . import views 


urlpatterns = [
    re_path(r'panel/$',views.PanelView.as_view(),name='panel'),
    re_path(r'firstbanner/$',views.FirstBannerView.as_view(),name='first-banner'),
    re_path(r'GalleryItems/$',views.GalleryItemView.as_view(),name='galleryitem'),
    re_path(r'secondbanner/$',views.SecondBannerView.as_view(),name='second-banner'),
    re_path(r'secondbanner/(?P<pk>\d+)/$',views.SecondBannerEditView.as_view(),name='second-banner-edit'),
    re_path(r'contactsection/$',views.ContactSectionView.as_view(),name='contact-section'),
    re_path(r'footer/$',views.FooterView.as_view(),name='footer'),
]
