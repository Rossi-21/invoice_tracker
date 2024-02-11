from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings

# email imports
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Internal imports
from .models import *
from .forms import *


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


def loginUser(request):
    return (request, login.html)
