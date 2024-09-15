from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import CertificateRequestForm, AddUserForm
from .models import CertificateRequest
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User 
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
import os
from django.http import FileResponse, Http404
from .models import ExcelFile
from .forms import ExcelFileForm
from django.contrib.auth.decorators import login_required

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

def index(request):
    return render(request, 'index.html')

def student_dashboard(request):
    if request.method == 'POST':
        form = CertificateRequestForm(request.POST)
        if form.is_valid():
            # Handle form data here
            form_data = form.cleaned_data
            return render(request, 'request_success.html', {'form_data': form_data})
    else:
        form = CertificateRequestForm()
    
    return render(request, 'student_dashboard.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def dashboard(request):
    notifications = CertificateRequest.objects.all().order_by('-submitted_at')[:10]  # Fetch the latest 10 requests
    return render(request, 'dashboard/dashboard.html', {'notifications': notifications})

def form_template_view(request):
    return render(request, 'dashboard/form_templates.html')

def notification_view(request):
    return render(request, 'dashboard/notifications.html')

def home_view(request):
    return render(request, 'dashboard/home.html')

def about_view(request):
    return render(request, 'dashboard/about.html')

def data_management_view(request):
    return render(request, 'dashboard/data_management.html')

@login_required
def settings_view(request):
    return render(request, 'dashboard/settings.html')


def password_reset(request):
    return render(request, 'password_reset.html')


def user_management(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the new user to the MySQL database
            messages.success(request, 'New user added successfully.')
            return redirect('user_management')
        else:
            messages.error(request, 'Failed to add user. Please check the form.')
    else:
        form = UserCreationForm()

    users = User.objects.all()  # Get all users from the database

    return render(request, 'dashboard/user_management.html', {'form': form, 'users': users})

# View to delete a user
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('user_management')

# View to update a user
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('user_management')
    else:
        form = UserCreationForm(instance=user)

    return render(request, 'dashboard/update_user.html', {'form': form, 'user': user})

def list_excel_files(request):
    excel_files = ExcelFile.objects.all()
    return render(request, 'dashboard/form_templates.html', {'excel_files': excel_files})

# View to handle file download
def download_excel_file(request, file_id):
    excel_file = get_object_or_404(ExcelFile, pk=file_id)
    response = HttpResponse(excel_file.file, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{excel_file.name}"'
    return response