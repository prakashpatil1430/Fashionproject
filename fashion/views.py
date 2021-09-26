from django.shortcuts import render
from django.views import View
from .models import Product, Customer, Cart, OrderPlaced
from django.shortcuts import render, redirect, HttpResponse
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.


class HomeView(View):
    def get(self, request):
        all_product = Product.objects.all()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'fashion/index2.html', context={'data': all_product, 'totalitem': totalitem})


def product_view(request, data=None):
    all_product = Product.objects.all()
    return render(request, 'fashion/index2.html', {'data': all_product})


class ProductDetailView(View):

    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'fashion/productdetail.html', {'product': product, 'totalitem': totalitem, 'item_already_in_cart': item_already_in_cart})


def perfume_view(request, data=None):

    all_product = Product.objects.all()
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        perfume = Product.objects.filter(category='P')
    elif data == 'Below1000':
        perfume = Product.objects.filter(
            category='P').filter(discounted_price__lt=1000)
    elif data == 'Above1000':
        perfume = Product.objects.filter(
            category='P').filter(discounted_price__gt=1000)

    return render(request, 'fashion/index2.html', {'perfume': perfume, 'totalitem': totalitem, 'data': all_product})


def tshirt_view(request, data=None):
    all_product = Product.objects.all()
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        tshirts = Product.objects.filter(category='TS')
    elif data == 'm-tshirt':
        tshirts = Product.objects.filter(category='TS').filter(brand=data)
    elif data == 'w-tshirt':
        tshirts = Product.objects.filter(category='TS').filter(brand=data)
    elif data == 'Below1000':
        tshirts = Product.objects.filter(
            category='TS').filter(discounted_price__lt=1000)
    elif data == 'Above1000':
        tshirts = Product.objects.filter(
            category='TS').filter(discounted_price__gt=1000)
    return render(request, 'fashion/index2.html', {'tshirts': tshirts, 'totalitem': totalitem, 'data': all_product})

def watch_view(request, data=None):
    all_product = Product.objects.all()
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        watches = Product.objects.filter(category='W')
    elif data == 'm-watch':
        watches = Product.objects.filter(category='W').filter(brand=data)
    elif data == 'w-match':
        tshirts = Product.objects.filter(category='W').filter(brand=data)
    elif data == 'Below1000':
        watches = Product.objects.filter(
            category='W').filter(discounted_price__lt=1000)
    elif data == 'Above1000':
        watches = Product.objects.filter(
            category='W').filter(discounted_price__gt=1000)
    return render(request, 'fashion/index2.html', {'watches': watches, 'totalitem': totalitem, 'data': all_product})



def shoes_view(request, data=None):
    all_product = Product.objects.all()
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))

    if data == None:
        shoes = Product.objects.filter(category='S')
    elif data == 'man-shoes':
        shoes = Product.objects.filter(category='S').filter(brand=data)
    elif data == 'women-shoes':
        shoes = Product.objects.filter(category='S').filter(brand=data)
    elif data == 'Above1000':
        shoes = Product.objects.filter(
            category='S').filter(discounted_price__gt=1000)
    elif data == 'Below1000':
        shoes = Product.objects.filter(
            category='S').filter(discounted_price__lt=1000)

    return render(request, 'fashion/index2.html', {'shoes': shoes, 'totalitem': totalitem, 'data': all_product})


def add_to_cart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Cart(user=user, product=product).save()
        return redirect('/cart')
    else:
        return redirect('/login')


def remove_cart(request, pk):
    user = request.user
    product = Product.objects.get(pk=pk)
    c = Cart.objects.get(Q(product=product) & Q(user=user))
    c.delete()
    return redirect('/cart')


class CustomerRegistrationView(View):

    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'fashion/customer_reg.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations!! Registered Successfully.')
            form.save()
        return render(request, 'fashion/customer_reg.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm()
        return render(request, 'fashion/profile.html', {'form': form, 'active': 'btn-primary', 'totalitem': totalitem})

    def post(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality,
                           city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(
                request, 'Congratulations!! Profile Updated Successfully.')
        return render(request, 'fashion/profile.html', {'form': form, 'active': 'btn-primary', 'totalitem': totalitem})


def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        addr = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount = amount+tempamount
                total_amount = amount + shipping_amount
        return render(request, 'fashion/checkout.html', {'addr': addr, 'cart_items': cart_items, 'total_amount': total_amount})
    else:
        return redirect('/login')


def address(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    addr = Customer.objects.filter(user=request.user)
    return render(request, 'fashion/address.html', {'addr': addr, 'active': 'btn-primary', 'totalitem': totalitem})


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount = amount+tempamount
                total_amount = amount + shipping_amount
            return render(request, 'fashion/addtocart.html', {'carts': cart, 'amount': amount, 'total_amount': total_amount})
        else:
            return render(request, 'fashion/emptycart.html')
    else:
        return redirect('/login')


def orders(request):
    user = request.user
    customer_id = user.id
    print(customer_id)
    cartid = Cart.objects.filter(user=user)
    customer = Customer.objects.get(id=customer_id)
    for cid in cartid:
        OrderPlaced(user=user, customer=customer,
                    product=cid.product, quantity=cid.quantity).save()
        # print("Order Saved")
        cid.delete()
        # print("Cart Item Deleted")
        return redirect("/orders")

    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'fashion/orders.html', {'order_placed': op})
