from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product
# Create your views here.

@login_required(login_url='user_login')
def index(request):
    return render(request,'dashboard/index.html')

@login_required(login_url='user_login')
def staff(request):
    return render(request,'dashboard/staff.html')

@login_required(login_url='user_login')
def product(request):
    return render(request,'dashboard/product.html')

@login_required(login_url='user_login')
def order(request):
    return render(request,'dashboard/order.html')

