from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/invoice', views.createInvoice, name="create-invoice"),
    path('create/department', views.createDepartment, name="create-department"),
    path('create/vendor', views.createVendor, name="create-vendor"),
    path('data/total', views.invoiceTotalView, name="invoice-total-view"),
    path('data/department', views.invoiceDepartmentView,
         name="invoice-department-view"),
    path('data/storesupplies', views.storeSupplies, name="store-supplies"),
    path('data/deli', views.deli, name="deli"),
    path('data/grocery', views.grocery, name="grocery"),
    path('data/meat', views.meat, name="meat"),
]
