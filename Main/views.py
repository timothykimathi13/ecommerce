from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def index(request):
    context = {}
    return render(request, 'Main/index.html',context)

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order  = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
 
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'Main/products.html',context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order  = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'Main/product_summary.html', context)
'''
def index(request):
    context = {}
    return render(request, 'Main/index.html',context)

def index(request):
    context = {}
    return render(request, 'Main/index.html',context)
    '''

def updateItem(request):
    data: json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:',productId )

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order,created = Order.objects.get_or_create(customer = customer, complete=False)
    OrderItem,created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        OrderItem.quantity = (OrderItem.quantity + 1)
    elif action == 'remove':
        OrderItem.quantity = (OrderItem.quantity - 1)

    OrderItem.save()

    if OrderItem.qunatity <= 0:
        OrderItem.delete()


    return  JsonResponse("Item was added", safe = False)
