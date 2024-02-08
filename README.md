# Invoice Tracking and Filtering App

## Overview

The Invoice Tracking and Filtering App is a web-based application developed using Django and Chartjs, designed to help users manage and filter invoices efficiently. The app provides features for creating invoices, filtering them based on various criteria, and visualizing the data through graphs.

## Features

- Filtering: Users can filter invoices based on department, date range, and vendor name.
- Total Calculation: The app calculates and displays the total sum of the filtered invoices.
- Graph Visualization: Graphs are generated to visualize total spend by vendor and department.

## **Getting Started**

### **Prerequisites**

- Python (version 3.6 or higher)
- Django (version 3.0 or higher)

## **Installation**

### **Clone the repository:**

git clone https://github.com/Rossi-21/invoice-tracking-app.git

### **Install the required dependencies:**

pip install -r requirements.txt

### **Apply migrations:**

```
python manage.py migrate
```

### **Create Superuser:**

```
python manage.py createsuperuser
```

### **Run the development server:**

- ```
  python manage.py runserver
  ```
- Open the app in your web browser: http://localhost:8000

### **Usage**

- Access the home page to filter and view invoices.
- Create new invoices using the "+Invoice" link.
- Invoices can be edited or deleted via the admin panel
- Visualize total spend by vendor and department through the provided links.

### **Code Structure**

views.py: Contains the views for home, invoice creation, and various data visualizations.
forms.py: Defines forms for creating and filtering invoices.
models.py: Defines the data models for invoices, vendors, and departments.
templates: Contains HTML templates for rendering pages.

### **Contributing**

Contributions are not accepted at this time.

### **License**

This project is licensed under the MIT License.
