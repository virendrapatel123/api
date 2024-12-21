# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('<int:pk>',views.detail),
    # path('form', views.form_page, name='product_list'),
    # path('product/<int:pk>/', views.product_detail, name='product_detail'),
    # path('table', views.product_table, name='product_table'),
    # path('table/<pk>',views.delete),
    # path('update/<pk>',views.update),
]
