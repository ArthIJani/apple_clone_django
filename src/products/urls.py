from django.urls import path
from . import views

urlpatterns = [
    path("store/", views.store_view, name='store'),
    path("mac/", views.mac_view, name='mac'),
    path("accessories/", views.accessories_view, name='accessories'),
]