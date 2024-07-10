# your_app/decorators.py
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

def login_required_message(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to perform this action.')
            return redirect(reverse('account_login') + '?next=' + request.path)
        return view_func(request, *args, **kwargs)
    return wrapper
