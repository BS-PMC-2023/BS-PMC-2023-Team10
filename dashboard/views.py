from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product,Order
from .forms import ProductForm,OrderForm
from .resources import ProductResource,OrderResource
import csv
from django.views import View
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='user_login')
def index(request):
    orders = Order.objects.all()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders':orders,
        'form':form,
    }

    return render(request,'dashboard/index.html',context)

@login_required(login_url='user_login')
def staff(request):
    workers = User.objects.all()
    context = {
        'workers':workers
    }

    return render(request,'dashboard/staff.html',context)

@login_required(login_url='user_login')
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers':workers,
    }
    return render(request, 'dashboard/staff_detail.html',context)

@login_required(login_url='user_login')
def product(request):
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items':items,
        'form':form,

        }
    return render(request,'dashboard/product.html',context)


@login_required(login_url='user_login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')


@login_required(login_url='user-login')
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_edit.html', context)

@login_required(login_url='user_login')
def order(request):
    orders = Order.objects.all()
    context = {
        'orders':orders,
    }
    return render(request,'dashboard/order.html',context)


class ExportDataView(View):
    def get(self, request):
        products = Product.objects.all()
        product_resource = ProductResource()
        dataset = product_resource.export(products)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        return response
    


class ExportOrderView(View):
    def get(self, request):
        orders = Order.objects.all()
        orders_resource = OrderResource()
        dataset = orders_resource.export(orders)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'
        return response
