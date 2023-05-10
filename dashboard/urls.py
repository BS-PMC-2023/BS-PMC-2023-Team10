from django.urls import path
from . import views
from .views import ExportDataView,ExportOrderView
urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/edit/<int:pk>/', views.product_edit,
         name='dashboard-product-edit'),
    path('order/', views.order, name='dashboard-order'),
    path('exportProducts/', ExportDataView.as_view(), name='exportProducts'),
    path('exportOrders/', ExportOrderView.as_view(), name='exportOrders'),
]
