# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('<int:pk>',views.detail),
    path('showroom',views.showroom_view.as_view(),name='showroom'),
    path('showroom/<int:pk>',views.showroom_detail.as_view())
]
