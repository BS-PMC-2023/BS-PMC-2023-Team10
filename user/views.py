from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
import csv
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            if is_email_in_csv(email):
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'User {username} has been created! Continue to login...')
                return redirect('dashboard-index')
            else:
                messages.error(request, 'Email not found in the allowed list.')
                return redirect('user_register')
        else:
            messages.error(request, 'Invalid form data.')
            return redirect('user_register')
    else:
        form = CreateUserForm()
    
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)



def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/profile_update.html', context)



def is_email_in_csv(email):
    with open('allowed_emails.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if email == row[0]:
                return True
    return False