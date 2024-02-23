from django.forms import ModelForm
from django import forms
from .models import *


class InvoiceCreateForm(ModelForm):
    class Meta:
        # Select your model
        model = Invoice
        # Choose the fields you want to show
        fields = ['vendor', 'department', 'total', 'date']
        # Apply Bootstrap CSS
        widgets = {
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    # Apply Bootstrap CSS and restrict to 10 digit input and 2 decimal places
    total = forms.DecimalField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_digits=10,
        decimal_places=2
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Filter vendors and departments based on the logged-in user
        if user:
            self.fields['vendor'].queryset = Vendor.objects.filter(user=user)
            self.fields['department'].queryset = Department.objects.filter(
                user=user)


class DepartmentCreateForm(ModelForm):
    class Meta:
        # Select your model
        model = Department
        # Choose the fields you want to show
        fields = ['name', 'number']
        # Apply Bootstrap CSS
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class VendorCreateForm(ModelForm):
    class Meta:
        # Select your model
        model = Vendor
        # Choose the fields you want to show
        fields = ['name']
        # Apply Bootstrap CSS
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class InvoiceFilterForm(forms.Form):
    # Set the form fields
    department = forms.ModelChoiceField(queryset=Department.objects.all(
    ), required=False, label='Department', empty_label='Select Department')
    date_start = forms.DateField(required=False, label='Start date', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    date_end = forms.DateField(required=False, label='End date', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    vendor_name = forms.ModelChoiceField(queryset=Vendor.objects.all(
    ), required=False, label='Vendor', empty_label="Select Vendor")

    # Apply Bootstrap CSS
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['department'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['vendor_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['date_start'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['date_end'].widget.attrs.update(
            {'class': 'form-control'})
        if user:
            self.fields['vendor_name'].queryset = Vendor.objects.filter(
                user=user)
            self.fields['department'].queryset = Department.objects.filter(
                user=user)
