from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('catalog', Catalog.as_view(), name='catalog'),
    path('search', Catalog.as_view(), name='search'),
    path('item/<str:slug>', GetItem.as_view(), name='item'),
]