from django.urls import path
from . import views

urlpatterns = [
    path('pedido/', views.pedido_view, name='pedido'),
]
