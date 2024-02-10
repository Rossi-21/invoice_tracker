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
    path('data/department/<str:department_name>', views.departmentSpendView,
         name="department-spend-view"),
]
