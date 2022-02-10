from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('catalog', Catalog.as_view(), name='catalog'),
    path('search', Catalog.as_view(), name='search'),
    path('item/<str:slug>', GetItem.as_view(), name='item'),
    path('item_ajax_buttons', ajax_buttons_for_add_or_delete_to_lists, name='item_ajax_buttons'),
    path('profile', profile, name='profile'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('signup', RegisterUser.as_view(), name='signup'),
]