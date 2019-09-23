from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    product = Product.objects.filter(Trending=True)
    new_arrival = Product.objects.filter(new_Arraivel=True)
    return render(request, "index.html", {'products': product, 'newarrival': new_arrival})


def Cart(request):
    products = Product.objects.filter(category=request.GET.get('category'))

    mycontext = {
        'products': products
    }
    return render(request, "pages/cart.html", mycontext)


def Shop(request):
    product = Product.objects.all()
    paginator = Paginator(product, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products
    }
    return render(request, "pages/shop.html", context)


def About(request):
    return render(request, "pages/about.html")


@login_required(login_url="/accounts/login/")
def CheckOut(request):
    return render(request, "pages/checkout.html")


def Product_Details(request, id, Product_slug):
    product = get_object_or_404(Product, id=id, Product_slug=Product_slug, available=True)
    return render(request, "pages/product-single.html", {'product': product})


def Contact(request):
    return render(request, "pages/contact.html")
