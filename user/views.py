from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, ProfileUpdateForm
from django.contrib import messages
import csv
from django.contrib.auth import logout
from dashboard.models import Order
# Create your views here.
from django.contrib.auth.views import LoginView

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            if is_email_in_csv(email):
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'User {username} has been created! Continue to login...')
                return redirect('user_login')
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
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('user_profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
    }
    return render(request, 'user/profile_update.html', context)



def is_email_in_csv(email):
    with open('allowed_emails.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if email == row[0]:
                return True
    return False



@login_required
def delete_user(request):
    user = request.user

    # Check if the user has any borrowed items
    has_borrowed_items = Order.objects.filter(staff=user).exists()

    if has_borrowed_items:
        #return redirect('profile')
        return render(request, 'user/profile.html', {'has_borrowed_items': True})

    if request.method == 'POST':
        user.delete()
        logout(request)  # Log out the user after deletion
        return redirect('user_register')  # Redirect to the registration page

    return render(request, 'user/delete_user.html', {'has_borrowed_items': False})