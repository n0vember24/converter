from django.urls import path

from converter.views import index

urlpatterns = [
    path('', index, name='index')
]
