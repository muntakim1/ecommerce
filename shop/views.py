from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "index.html")


def Cart(request):
    return render(request, "pages/cart.html")


def Shop(request):
    product = Product.objects.all()
    paginator = Paginator(product, 1)
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
