from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product,Order
from .forms import ProductForm,OrderForm
from .resources import ProductResource,OrderResource
from django.db.models import F
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.http import JsonResponse



# Create your views here.


def get_products_by_category(request):
    category = request.GET.get('category')

    # Retrieve products based on the selected category
    products = Product.objects.filter(category=category)

    # Prepare the data to be sent as a JSON response
    products_data = []
    for product in products:
        product_data = {
            'name': product.name,
            'quantity': product.quantity,
        }
        products_data.append(product_data)

    response_data = {
        'products': products_data,
    }

    return JsonResponse(response_data)


@login_required(login_url='user_login')
def index(request):
    products = Product.objects.filter(quantity__gt=0)
    product_count = products.count()
    orders = Order.objects.all()
    order_count = orders.count()
    customers = User.objects.exclude(username='admin')
    customer_count = customers.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.staff = request.user
            order.save()
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
    products = Product.objects.filter(quantity__gt=0)
    product_count = products.count()
    orders = Order.objects.all()
    order_count = orders.count()
    customers = User.objects.exclude(username='admin')
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
    customer_count = User.objects.exclude(username='admin').count()
    products = Product.objects.filter(quantity__gt=0)
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
    customer_count = User.objects.exclude(username='admin').count()
    products = Product.objects.filter(quantity__gt=0)
    product_count = products.count()
    orders = Order.objects.all()
    order_count = orders.count()
    items = Product.objects.all()
    unique_categories = set(products.values_list('category', flat=True))
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
        'unique_categories':unique_categories,

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
    products = Product.objects.filter(quantity__gt=0)
    product_count = products.count()
    orders = Order.objects.all()
    order_count = orders.count()
    customers = User.objects.exclude(username='admin')
    customer_count = customers.count()
    context = {
        'orders':orders,
        'customer_count':customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request,'dashboard/order.html',context)

def extend_order(request,order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        return_date = request.POST.get('return_date')
        order.extendedDate = return_date
        order.extendRequested = 'Pending'
        order.save()
        return redirect('dashboard-index')
    return render(request, 'dashboard/extend_order.html', {'order': order})



def extend_approve_deny(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status == 'Approve':
            order.extendRequested = 'Approved'
            order.returnDate=order.extendedDate
        elif status == 'Deny':
            order.extendRequested = 'Denied'
        order.save()
        return redirect('dashboard-order')
    return render(request, 'dashboard/extend_approve_deny.html', {'order': order})






@login_required(login_url='user_login')
def approve_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Approved'
    order.save()
    product = order.product
    product.quantity = F('quantity') - order.quantity
    product.save()
    return redirect('dashboard-order')

def finish_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Finished'
    order.save()
    product = order.product
    product.quantity = F('quantity') + order.quantity
    product.save()
    return redirect('dashboard-order')


def remove_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('dashboard-order')


@login_required(login_url='user_login')
def deny_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Denied'
    order.save()
    return redirect('dashboard-order')

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
