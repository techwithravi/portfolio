from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product, contactenquiry
from django.contrib.auth.models import User



# Create your views here.
def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        n = request.POST['uname']
        p = request.POST['upass']

        u = authenticate(username=n, password=p)

        if u is not None:
            login(request, u)
            return redirect('/product')
        else:
            context = {}
            context['errmsg'] = 'Invalid UserName and Password'
            return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/login')


def search(request):
    query = request.GET['query']

    pname = Product.objects.filter(name__icontains=query)
    pcat = Product.objects.filter(cat__icontains=query)
    pdetail = Product.objects.filter(pdetail__icontains=query)

    allprod = pname.union(pcat, pdetail)
    context = {}

    if allprod.count() == 0:
        context['errmsg'] = 'Dog not found'

    context['data'] = allprod
    return render(request, 'index.html', context)


def product(request):
    p = Product.objects.filter(is_active=True)
    context = {}
    context['data'] = p
    return render(request, 'index.html', context)


def landing(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        se = contactenquiry(name=name, email=email, message=message)
        se.save()
    return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        context = {}
        n = request.POST['uname']
        p = request.POST['upass']
        cp = request.POST['ucpass']

        if n == '' or p == '' or cp == '':
            context['errmsg'] = 'Field can not be Null'
            return render(request, 'register.html', context)

        elif len(p) < 8:
            context['errmsg'] = 'Password must be 8 character'
            return render(request, 'register.html', context)

        elif p != cp:
            context['errmsg'] = 'Password and confirm password must be same'
            return render(request, 'register.html', context)

        else:
            try:
                u = User.objects.create(username=n, email=n)
                u.set_password(p)
                u.save()
                context['success'] = 'User Created Successfully'
                return render(request, 'register.html', context)
            except Exception:
                context['errmsg'] = "User Already Exists, Please Login..!"
                return render(request, 'register.html', context)


def productdetail(request, pid):
    p = Product.objects.filter(id=pid)
    context = {}
    context['data'] = p
    return render(request, 'product_detail.html', context)


def orderhistory(request):
    return render(request, 'orderhistory.html')

def addtocart(request,pid):
    if request.user.is_