from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('agregar/', views.agregar_membresia, name='agregar_membresia'),
    path('editar/<int:id>/', views.editar_membresia, name='editar_membresia'),
    path('borrar/<int:id>/', views.borrar_membresia, name='borrar_membresia'),
]
