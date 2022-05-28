from random import randint

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Order, Product


@login_required(login_url="auth/login/")
@csrf_exempt
def products(request, season):
    categories = Category.objects.filter(season=season)
    if request.method == "GET":
        products = []
        for category in categories:
            products.extend(Product.objects.filter(category=category))
    if request.method == "POST":
        text = request.POST.get("search-product")
        products = Product.objects.filter(
            name__icontains=text, category__season=season
        )

    context = {"categories": categories, "products": products}
    return render(request, "product.html", context)


@login_required(login_url="auth/login/")
def product_detail(request, id, season):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        is_product_in_cart = Order.objects.filter(product_id=product)
        if is_product_in_cart:
            is_product_in_cart.delete()
        quantity = request.POST.get("num-product")
        Order.objects.create(
            user_id=request.user,
            product_id=product,
            quantity=quantity,
            total_cost=product.cost * int(quantity),
        )
    return render(request, "product-detail.html", {"product": product})


@login_required(login_url="auth/login/")
def main(request):
    return render(request, "index.html")


@login_required(login_url="auth/login/")
def contact(request):
    return render(request, "contact.html")


@login_required(login_url="auth/login/")
def about(request):
    return render(request, "about.html")


@login_required(login_url="auth/login/")
def cart(request):
    orders = Order.objects.filter(user_id=request.user.id)
    cart_total = Order.objects.filter(user_id=request.user.id).aggregate(
        Sum("total_cost")
    )
    if cart_total["total_cost__sum"] is None:
        cart_total = 0
    else:
        cart_total = cart_total["total_cost__sum"]
    return render(
        request, "cart.html", {"orders": orders, "cart_total": cart_total}
    )


@login_required(login_url="auth/login/")
def checkout(request):
    orders = Order.objects.filter(user_id=request.user.id)
    orders.delete()
    return redirect("cart")
