from django.urls import path, include
from Secundaria.views import *

urlpatterns = [
    path('', home, name='home'),
]
