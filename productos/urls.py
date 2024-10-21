from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar_productos, name='listar_productos'),
    path('registrar/', views.registrar_producto, name='registrar_producto'),
    path('insertar/', views.insertar_producto, name='insertar_producto'),
    path('actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]
