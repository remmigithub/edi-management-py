from django.shortcuts import render,redirect
from .models import Product, Contact, Orders
from math import ceil
import json
from django.http import HttpResponse
# Create your views here.

def add_cart(request,myid):
   total=0
   pro=Product.objects.filter(id=myid)
   for q in pro:
        pro_cat=q.category
        qty=q.qty
        price=q.price
       
   qty=qty+1
   total=qty*price
   pro.update(cart=True,qty=qty,total=total)
   return redirect('shop:home',cat_name=pro_cat)


def update_cart(request,myid,oper):
    pro=Product.objects.filter(id=myid)
    for q in pro:
        pro_cat=q.category
        qty=q.qty
        total=q.total
        price=q.price

    if oper=='minus':
        qty=qty-1
        if qty==0:
            pro.update(qty=0,total=0,cart=False)
        total=qty*price
        pro.update(qty=qty,total=total)
    else:
        qty=qty+1
        total=qty*price
        pro.update(qty=qty,total=total)

    return redirect('shop:home',cat_name=pro_cat)

def index(request):
    return render(request, 'shop/home.html')

def shop(request,cat_name):
    allProds = []
    prod = Product.objects.filter(category=cat_name)
    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
   return render(request, 'shop/tracker.html')


def search(request):
    # return HttpResponse('helllo searched page is here!')
    searched=request.GET.get('q')
    products=Product.objects.filter(product_name__contains=searched)
    return render(request, 'shop/search.html',{'products':products})


def productView(request, myid):

    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})


def checkout(request):
    qty=0
    item=''
    every=''
    data=Product.objects.filter(qty__gt=0)
    for d in data:
        qty=d.qty
        item=d.product_name
        every=every+item+'--'+str(qty)+','

    total=0
    for i in data:
        total+=i.total
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=every,qty=qty,name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        data=Product.objects.filter(qty__gt=0)
        data.update(qty=0,cart=False,total=0)
        return render(request, 'shop/checkout.html',{'thank':thank})
    return render(request, 'shop/checkout.html',{'data':data,'total':total})