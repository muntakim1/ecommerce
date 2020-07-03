from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, Cart,OderTracking,Transactions
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    product = Product.objects.filter(Trending=True)
    new_arrival = Product.objects.filter(new_Arraivel=True)
    return render(request, "index.html", {'products': product, 'newarrival': new_arrival})


def Cart_View(request):
    products = Product.objects.filter(category=request.GET.get('category'))
    new_arrival = Product.objects.filter(new_Arraivel=True)
    mycontext = {
        'products': new_arrival
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


@login_required(login_url="/login/")
def CheckOut(request):
    current_user = request.user
    if request.method == 'POST':
        transactions = Transactions.objects.get_or_create(user=current_user)
        fname = request.POST['first_name']
        lname =request.POST['last_name']
        country =request.POST['Country']
        streetaddress =request.POST['streetaddress']
        appartment =request.POST['appartment']
        town =request.POST['town']
        postcode =request.POST['postcode']
        phone =request.POST['phone']
        total =request.POST['money']
        email =request.POST['email']
        payment =request.POST['payment']
        
        transactions[0].first_name=fname
        transactions[0].last_name=lname
        transactions[0].state_country=country
        transactions[0].street_Address=streetaddress
        transactions[0].appertment=appartment
        transactions[0].town=town
        transactions[0].postcode=postcode
        transactions[0].phone=phone
        transactions[0].email=email
        transactions[0].payment_Method=payment
        transactions[0].Total=total
        print(transactions[0].appertment)
        transactions[0].save() 
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "pages/checkout.html",context)

@login_required(login_url="/login/")
def OrderStatus(request):
    Ordertracker = OderTracking.objects.filter()
    context ={
        'OderTracking':Ordertracker
    }
    return render(request, "accounts/ProductDeliveryStatus.html",context)

def Product_Details(request, id, Product_slug):
    product = get_object_or_404(Product, id=id, Product_slug=Product_slug, available=True)
    return render(request, "pages/product-single.html", {'product': product})


def Contact(request):
    return render(request, "pages/contact.html")

