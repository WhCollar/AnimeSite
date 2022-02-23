from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('catalog', Catalog.as_view(), name='catalog'),
    path('search', Catalog.as_view(), name='search'),
    path('item/<str:slug>', GetItem.as_view(), name='item'),
    path('profile/<int:pk>', Profile.as_view(), name='profile'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('signup', RegisterUser.as_view(), name='signup'),
]
