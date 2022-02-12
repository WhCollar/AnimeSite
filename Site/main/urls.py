from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('catalog', Catalog.as_view(), name='catalog'),
    path('search', Catalog.as_view(), name='search'),
    path('item/<str:slug>', GetItem.as_view(), name='item'),
    path('item_ajax_buttons', item_ajax_buttons, name='item_ajax_buttons'),
    path('item_ajax_buttons_validate', item_ajax_buttons_validate, name='item_ajax_buttons_validate'),
    path('profile', profile, name='profile'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('signup', RegisterUser.as_view(), name='signup'),
]