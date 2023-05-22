from django.urls import path
from . import views
from .views import ExportDataView,ExportOrderView
urlpatterns = [ 
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/edit/<int:pk>/', views.product_edit, name='dashboard-product-edit'),
    path('order/', views.order, name='dashboard-order'),
    path('order/approve/<int:order_id>/', views.approve_order, name='approve_order'),
    path('order/deny/<int:order_id>/', views.deny_order, name='deny_order'),
    path('order/finish/<int:order_id>/', views.finish_order, name='finish_order'),
    path('order/remove/<int:order_id>/', views.remove_order, name='remove_order'),
    path('order/extend/<int:order_id>/', views.extend_order, name='extend_order'),
    path('order/extend_approve_deny/<int:order_id>/', views.extend_approve_deny, name='extend_approve_deny'),
    path('exportProducts/', ExportDataView.as_view(), name='exportProducts'),
    path('exportOrders/', ExportOrderView.as_view(), name='exportOrders'),
    path('get_products_by_category/', views.get_products_by_category, name='get_products_by_category'),

]
