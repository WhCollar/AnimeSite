from django.urls import path
from .ajax_views import *


urlpatterns = [
    path('item_ajax_buttons', item_ajax_buttons, name='item_ajax_buttons'),
    path('item_ajax_buttons_validate', item_ajax_buttons_validate, name='item_ajax_buttons_validate'),
    path('registration_form_validate', registration_form_validate, name='registration_form_validate'),
    path('create_comment', create_comment, name='create_comment'),
    path('view_comment', view_comment, name='view_comment'),
    path('view_response_comment', view_response_comment, name='view_response_comment'),
]