# Invoice Tracking and Filtering App

## Overview

The Invoice Tracking and Filtering App is a web-based application developed using Django and Chartjs, designed to help users manage and filter invoices efficiently. The app provides features for creating invoices, vendors, and departments. Filtering invoices based on various criteria, and visualizing the data through graphs.

## Features

- Filtering: Users can filter invoices based on department, date range, and vendor name.
- Total Calculation: The app calculates and displays the total sum of the filtered invoices.
- Graph Visualization: Graphs are generated to visualize total spend by vendor and department.

## **Getting Started**

### **Prerequisites**

- A working internet connection

## **Registration**

### **Visit:**

```
http://ec2-54-187-17-171.us-west-2.compute.amazonaws.com/register/
```

- Create a username
- Enter a valid email address
- Create a vaild password

### **Usage**

- Use the Get Started dropdown to create Vendors, Departments, and Invoices.
- Invoices can be edited or deleted via the edit link on the home page.
- Departments and Vendors can be edited using the View dropdown.
- Visit the Data dropdown to visualize your spend.

### **Code Structure**

- **views.py**: Contains the views for home, invoice creation, and various data visualizations.
- **forms.py**: Defines forms for creating and filtering invoices.
- **models.py**: Defines the data models for invoices, vendors, and departments.
- **templates**: Contains HTML templates for rendering pages.
