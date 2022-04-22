from django.urls import path
from .views import index, take, results

urlpatterns = [
    path('', index, name='index'),
    path('take', take, name='take'),
    path('results', results, name='results'),
]
