from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse
from .models import Product,Order,DamageReport,Message,Reservation
from .forms import ProductForm,OrderForm,DamageReportForm,ReservationForm
from .resources import ProductResource,OrderResource
from django.db.models import F
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Sum
from django.core.exceptions import PermissionDenied
from import_export.formats import base_formats

def staff_required(view_func):
    @login_required(login_url='user_login')
    @user_passes_test(lambda u: u.is_staff, login_url='user_login')
    def wrapper(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper



# Create your views here.

def reserve_studio(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.customer = request.user
            reservation.save()
            return redirect('dashboard-index')
    else:
        form = ReservationForm()

    return render(request, 'dashboard/reserve_studio.html', {'form': form})

@staff_required
def approve_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.status = 'Approved'
        reservation.save()
        return redirect('view_request')
    return render(request, 'dashboard/view_request.html', {'reservation': reservation})


@staff_required
def deny_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.status = 'Denied'
        reservation.save()
        return redirect('view_request')
    return render(request, 'dashboard/view_request.html', {'reservation': reservation})


@staff_required
def remove_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.is_visible_to_manager = False
        reservation.save()
        return redirect('view_request')
    return render(request, 'dashboard/view_request.html', {'reservation': reservation})


def remove_reservation_student(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.is_visible_to_student = False
        reservation.save()
        return redirect('view_request_student')
    return render(request, 'dashboard/view_request_student.html', {'reservation': reservation})

def view_request_student(request):
    messages = Message.objects.filter(customer=request.user)  # Filter messages by the current user
    reservations = Reservation.objects.filter(customer=request.user)
    return render(request, 'dashboard/view_request_student.html', {'messages': messages, 'reservations': reservations})

@staff_required
def remove_request(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        message.is_visible_to_manager = False
        message.save()
        return redirect('view_request')
    return render(request, {'message': message})

def remove_request_student(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        message.is_visible_to_student = False
        message.save()
        return redirect('view_request_student')
    return render(request, {'message': message})


@staff_required
def view_request(request):
    if not request.user.is_staff:
        raise PermissionDenied
    messages = Message.objects.all()
    reservations = Reservation.objects.all()

    return render(request, 'dashboard/view_request.html', {'messages': messages, 'reservations': reservations})



def send_request(request):
    products = Product.objects.all()
    
    if request.method == 'POST':
        product_id = request.POST.get('product')
        product = get_object_or_404(Product, pk=product_id)
        message = request.POST.get('message')
        Message.objects.create(
            customer=request.user,
            product=product,
            message=message
        )
        return redirect('dashboard-index')

    return render(request, 'dashboard/send_request.html', {'products': products})


def reserve_request(request):
    products = Product.objects.all()
    
    if request.method == 'POST':
        product_id = request.POST.get('product')
        product = get_object_or_404(Product, pk=product_id)
        message = request.POST.get('message')
        Message.objects.create(
            customer=request.user,
            product=product,
            message=message
        )
        return redirect('dashboard-index')

    return render(request, 'dashboard/reserve_request.html', {'products': products})

@staff_required
def approve_request(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        message.status = 'Approved'
        message.save()
        return redirect('view_request')
    
@staff_required
def deny_request(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        # Perform your denial logic here
        message.status = 'Denied'
        message.save()
        return redirect('view_request')



def report_damage(request, order_id):
    order = Order.objects.get(id=order_id)
    product_name = order.product.name

    if request.method == 'POST':
        form = DamageReportForm(request.POST)
        if form.is_valid():
            damage_report = form.save(commit=False)
            damage_report.order = order
            damage_report.save()
            order.is_reported = True
            order.save()

            return redirect('dashboard-index')
    else:
        form = DamageReportForm(product_name=product_name)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/report_damage.html', context)

@staff_required
def view_damage_report(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    damage_report = DamageReport.objects.get(order=order)
    context = {'order': order, 'damage_report': damage_report}
    return render(request, 'dashboard/view_damage_report.html', context)



def get_products_by_category(request):
    category = request.GET.get('category')
    products = Product.objects.filter(category=category)
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
    product_count = Product.objects.aggregate(product_count=Sum('quantity'))['product_count']
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

@staff_required
def staff(request):
    products = Product.objects.filter(quantity__gt=0)
    product_count = Product.objects.aggregate(product_count=Sum('quantity'))['product_count']
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

@staff_required
def staff_detail(request,pk):
    customers = User.objects.get(id=pk)
    customer_count = User.objects.exclude(username='admin').count()
    products = Product.objects.filter(quantity__gt=0)
    product_count = Product.objects.aggregate(product_count=Sum('quantity'))['product_count']
    orders = Order.objects.all()
    order_count = orders.count()
    context = {
        'customers':customers,
        'customer_count':customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/staff_detail.html',context)

@staff_required
def product(request):
    customer_count = User.objects.exclude(username='admin').count()
    products = Product.objects.filter(quantity__gt=0)
    product_count = Product.objects.aggregate(product_count=Sum('quantity'))['product_count']
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

@staff_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')


@staff_required
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

@staff_required
def order(request):
    products = Product.objects.filter(quantity__gt=0)
    product_count = Product.objects.aggregate(product_count=Sum('quantity'))['product_count']
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


@staff_required
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






@staff_required
def approve_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Approved'
    order.save()
    product = order.product
    product.quantity = F('quantity') - order.quantity
    product.save()
    return redirect('dashboard-order')

@staff_required
def finish_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Finished'
    order.save()
    product = order.product
    product.quantity = F('quantity') + order.quantity
    product.save()
    return redirect('dashboard-order')

@staff_required
def remove_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    order.delete()
    return redirect('dashboard-order')


@staff_required
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
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="items.xlsx"'
        export_format = base_formats.XLSX()
        export_data = export_format.export_data(dataset)
        response.write(export_data)
        return response
    


class ExportOrderView(View):
    def get(self, request):
        orders = Order.objects.all()
        orders_resource = OrderResource()
        dataset = orders_resource.export(orders)
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="orders.xlsx"'
        
        export_format = base_formats.XLSX()
        export_data = export_format.export_data(dataset)
        
        response.write(export_data)
        
        return response



