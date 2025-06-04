from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def login_view(request):
    """Handle user login.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    # First check if user is already register
    if request.user.is_authenticated:
        return redirect(request.GET.get('next', 'home'))
    
    # If Not login then Try login
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Logout view to log out the user
# and redirect to the login page with a success message
def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

# Registration view to handle user registration
# It uses a custom user creation form to register new users
def register_view(request):
    """
    Handle user registration.

    This view processes the user registration form. If the form is valid, the user's data is saved,
    and they are redirected to the login page with a success message. If the form is invalid, an error 
    message is displayed.

    Args:
        request (HttpRequest): The HTTP request object, which contains the form data in case of a POST request.

    Returns:
        HttpResponse: The HTTP response object, which renders the registration page or redirects to the login page.
    """

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Now you can log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})