from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product,Order
from .forms import ProductForm,OrderForm
from .resources import ProductResource,OrderResource
import csv
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='user_login')
def index(request):
    products = Product.objects.all()
    product_count = products.count()
    orders = Order.objects.all()
    order_count = orders.count()
    customers = User.objects.all()
    customer_count = customers.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'orders': orders,
        'products': products,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user_login')
def staff(request):
    products = Product.objects.all()
    product_count = products.count()
    orders = Order.objects.all()
    order_count = orders.count()
    customers = User.objects.all()
    customer_count = customers.count()
    context = {
        'customers':customers,
        'customer_count':customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request,'dashboard/staff.html',context)

@login_required(login_url='user_login')
def staff_detail(request,pk):
    customers = User.objects.get(id=pk)
    customer_count = User.objects.all().count()
    products = Product.objects.all()
    product_count = products.count()
    orders = Order.objects.all()
    order_count = orders.count()
    context = {
        'customers':customers,
        'customer_count':customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/staff_detail.html',context)

@login_required(login_url='user_login')
def product(request):
    customer_count = User.objects.all().count()
    products = Product.objects.all()
    product_count = products.count()
    orders = Order.objects.all()
    order_count = orders.count()
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added!')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items':items,
        'form':form,
        'customer_count':customer_count,
        'product_count': product_count,
        'order_count': order_count,

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
    products = Product.objects.all()
    product_count = products.count()
    orders = Order.objects.all()
    order_count = orders.count()
    customers = User.objects.all()
    customer_count = customers.count()
    context = {
        'orders':orders,
        'customer_count':customer_count,
        'product_count': product_count,
        'order_count': order_count,
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
