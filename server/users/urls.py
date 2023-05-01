from django.urls import path
from .views import user_list, adduser_list

urlpatterns = [
    path('users/', user_list),
    path('adduser/', adduser_list)
]