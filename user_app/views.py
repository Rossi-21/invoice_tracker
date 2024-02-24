from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404


# email imports
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Internal imports
from invoice_app.models import *
from .models import *
from .forms import *

# Register User Function


def registerUser(request):
    # Display the user creation form
    form = CreateUserForm()

    if request.method == 'POST':
        # Grab the submitted info from the form
        form = CreateUserForm(request.POST)

        if form.is_valid():
            # Save the user & log them in
            user = form.save()
            login(request, user)
            # Send the new user and email
            subject = 'Thanks for trying my app !'
            html_message = render_to_string(
                'registration_email.html', {'user': user})
            plain_message = strip_tags(html_message)
            from_email = 'email_address'
            to = [user.email]

            send_mail(subject, plain_message, from_email,
                      to, html_message=html_message)

            # Redirect them to the dashboard
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


# Login User function
def loginUser(request):
    if request.method == "POST":
        # Get the username and password from the database
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Verify the username and password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If the user exists log them in
            login(request, user)
            # Redirect to the dashboard
            return redirect('home')

        else:
            # If the user does not exist, display an error message
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'login.html')


@login_required
# View User function
def viewUser(request, id):
    departments = Department.objects.filter(user=request.user)
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    context = {
        'user': user,
        'departments': departments,
        'profile': profile,
    }

    return render(request, 'viewUser.html', context)


@login_required
# Update User function
def updateUser(request, id):
    departments = Department.objects.filter(user=request.user)
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)
    form = CreateUserForm(instance=user)

    if request.method == 'POST':
        form = CreateUserForm(request.POST or None, instance=user)

        if form.is_valid():
            # Save the edited form to the database
            form.save()
            # Login the user
            login(request, user)
            # return to the View User page
            return redirect(reverse('view-user', args=[user.id]))

    context = {
        'user': user,
        'departments': departments,
        'profile': profile,
        'form': form,
    }

    return render(request, 'updateUser.html', context)


@login_required
# Logout User Function
def logoutUser(request):
    # Logout the User
    logout(request)
    # Send the User back to the Login page
    return redirect('loginUser')


@login_required
# Delete User Page
def deleteCheck(request):
    return render(request, 'deleteUser.html')


@login_required
# Delete User Function
def deleteUser(request, id):
    # Get the User by id
    user = User.objects.get(id=id)
    # Remove the User from the database
    user.delete()
    # Send the User to the Dashboard
    return redirect('registerUser')
