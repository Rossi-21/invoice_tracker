from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/invoice', views.createInvoice, name="create-invoice"),
    path('create/department', views.createDepartment, name="create-department"),
    path('create/vendor', views.createVendor, name="create-vendor"),
    path('data/vendor', views.invoiceTotalView, name="invoice-total-view"),
    path('data/department', views.invoiceDepartmentView,
         name="invoice-department-view"),
    path('data/department/<str:department_name>', views.departmentSpendView,
         name="department-spend-view"),
    path('view/department', views.viewDepartment, name="view-department"),
    path('veiw/vendor', views.viewVendor, name="view-vendor"),
    path('update/invoice/<int:id>', views.updateInvoice, name="update-invoice"),
    path('update/department/<int:id>',
         views.updateDepartment, name="update-department"),
    path('update/vendor/<int:id>',
         views.updateVendor, name="update-vendor"),
    path('delete/invoice/<int:id>', views.deleteInvoice, name="delete-invoice"),
    path('delete/department/<int:id>',
         views.deleteDepartment, name="delete-department"),
    path('delete/vendor/<int:id>',
         views.deleteVendor, name="delete-vendor"),
]
