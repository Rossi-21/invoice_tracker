from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


@login_required
def home(request):
    departments = Department.objects.filter(user=request.user)
    # Get all invoices from the Database
    invoices = Invoice.objects.filter(user=request.user)
    # Select form from forms.py for the view
    form = InvoiceFilterForm()
    # Sum Variable
    total_sum = 0

    if request.method == 'POST':
        departments = Department.objects.all()
        # Grab the form for processing
        form = InvoiceFilterForm(request.POST)
        if form.is_valid():
            # Build the filter parameters based on form input
            filter_params = {}
            if form.cleaned_data['department']:
                filter_params['department__name__icontains'] = form.cleaned_data['department']
            if form.cleaned_data['date_start']:
                filter_params['date__gte'] = form.cleaned_data['date_start']
            if form.cleaned_data['date_end']:
                filter_params['date__lte'] = form.cleaned_data['date_end']
            if form.cleaned_data['vendor_name']:
                filter_params['vendor__name__icontains'] = form.cleaned_data['vendor_name']

            # Query the database with the filter parameters
            filtered_invoices = Invoice.objects.filter(**filter_params)

            if filtered_invoices:
                # Add the totals together to display the correct sum
                total_sum = round(filtered_invoices.aggregate(
                    Sum('total'))['total__sum'] or 0, 2)

            return render(request, 'index.html', {'invoices': filtered_invoices, 'form': form, 'total_sum': total_sum, 'departments': departments})

    context = {
        'invoices': invoices,
        'form': form,
        'total_sum': total_sum,
        'departments': departments,
    }
    return render(request, 'index.html', context)


@login_required
def createInvoice(request):
    departments = Department.objects.filter(user=request.user)
    # Select form from forms.py for the view
    form = InvoiceCreateForm(user=request.user)
    # Get the last three invoices form the database
    invoices = Invoice.objects.filter(user=request.user).order_by('-id')[:3]

    if request.method == 'POST':
        # Grab the form for processing
        form = InvoiceCreateForm(request.POST, user=request.user)
        if form.is_valid():
            invoice = form.save(commit=False)
            # Associate the current User with the department being created
            invoice.user = request.user
            # If the form is valid save it to the database
            form.save()

            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'invoices': invoices,
        'departments': departments,
    }
    return render(request, 'createInvoice.html', context)


@login_required
def createDepartment(request):
    departments = Department.objects.filter(user=request.user)
    # Select form from forms.py for the view
    form = DepartmentCreateForm()

    if request.method == 'POST':
        # Grab the form for processing
        form = DepartmentCreateForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            # Associate the current User with the department being created
            department.user = request.user
            # If the form is valid save it to the database
            form.save()
            messages.success(request, 'Department created successfully!')
            print(form)
            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'departments': departments,
    }
    return render(request, 'createDepartment.html', context)


@login_required
def createVendor(request):
    departments = Department.objects.filter(user=request.user)
    # Select form from forms.py for the view
    form = VendorCreateForm()

    if request.method == 'POST':
        # Grab the form for processing
        form = VendorCreateForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            # Associate the current User with the department being created
            vendor.user = request.user
            # If the form is valid save it to the database
            form.save()
            messages.success(request, 'Vendor created successfully!')
            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'departments': departments,
    }
    return render(request, 'createVendor.html', context)


@login_required
def invoiceTotalView(request):
    departments = Department.objects.filter(user=request.user)
    # Aggregate data by vendor and calculate the sum of invoice totals
    vendor_totals = Invoice.objects.filter(user=request.user).values(
        'vendor__name').annotate(total_sum=Sum('total'))

    # Extract labels and data for Chart.js
    vendor_labels = [entry['vendor__name'] for entry in vendor_totals]
    total_sums = [entry['total_sum'] for entry in vendor_totals]

    context = {
        'departments': departments,
        'vendor_labels': vendor_labels,
        'total_sums': total_sums,
    }
    return render(request, 'invoiceTotalView.html', context)


@login_required
def invoiceDepartmentView(request):
    departments = Department.objects.filter(user=request.user)
    # Calulate total spend for each department
    department_totals = Invoice.objects.filter(user=request.user).values(
        'department__name').annotate(total_spend=Sum('total'))
    # Extract data for Chart.js
    department_labels = [entry['department__name']
                         for entry in department_totals]
    total_spend = [entry['total_spend'] for entry in department_totals]

    context = {
        'department_labels': department_labels,
        'total_spend': total_spend,
        'departments': departments,
    }
    return render(request, 'invoiceDepartmentView.html', context)


@login_required
def departmentSpendView(request, department_name):
    departments = Department.objects.filter(user=request.user)
    # Get the Department
    department = Department.objects.filter(
        user=request.user).get(name=department_name)
    # Retrieve invoices from the specified department
    invoices = Invoice.objects.filter(department=department).order_by('date')

    # Extract data for Chart.js
    dates = [invoice.date.strftime('%m-%d') for invoice in invoices]
    invoice_totals = [invoice.total for invoice in invoices]

    context = {
        'dates': dates,
        'invoice_totals': invoice_totals,
        'department_name': department.name,
        'departments': departments,
    }

    return render(request, 'department_spend.html', context)


@login_required
def viewDepartment(request):
    user = request.user
    print(user)
    departments = Department.objects.filter(user=request.user)
    print(departments)
    context = {
        'user': user,
        'departments': departments
    }
    return render(request, 'viewDepartment.html', context)


@login_required
def viewVendor(request):
    departments = Department.objects.filter(user=request.user)
    vendors = Vendor.objects.filter(user=request.user)

    context = {
        'vendors': vendors,
        'departments': departments
    }
    return render(request, 'viewVendor.html', context)


@login_required
def updateInvoice(request, id):
    departments = Department.objects.filter(user=request.user)
    invoice = Invoice.objects.get(id=id)
    form = InvoiceCreateForm(instance=invoice)

    if request.method == "POST":
        form = InvoiceCreateForm(request.POST, instance=invoice)

        if form.is_valid():
            form.save()

            return redirect("home")

    context = {
        'departments': departments,
        'invoice': invoice,
        'form': form,

    }
    return render(request, 'updateInvoice.html', context)


@login_required
def updateDepartment(request, id):
    departments = Department.objects.filter(user=request.user)
    department = Department.objects.get(id=id)
    form = DepartmentCreateForm(instance=department)

    if request.method == "POST":
        form = DepartmentCreateForm(request.POST, instance=department)

        if form.is_valid():
            form.save()

            return redirect("view-department")

    context = {
        'departments': departments,
        'department': department,
        'form': form,

    }
    return render(request, 'updateDepartment.html', context)


@login_required
def updateVendor(request, id):
    departments = Department.objects.filter(user=request.user)
    vendor = Vendor.objects.get(id=id)
    form = VendorCreateForm(instance=vendor)

    if request.method == "POST":
        form = VendorCreateForm(request.POST, instance=vendor)

        if form.is_valid():
            form.save()

            return redirect("view-vendor")

    context = {
        'departments': departments,
        'vendor': vendor,
        'form': form,

    }
    return render(request, 'updateVendor.html', context)
