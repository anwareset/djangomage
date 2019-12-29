from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seek', views.seek, name='seek'),
    path('rotate', views.rotate, name='rotate'),
    path('flip', views.flip, name='flip'),
    path('crop', views.crop, name='crop'),
    path('scale', views.scale, name='scale'),
    path('invert', views.invert, name='invert'),
]