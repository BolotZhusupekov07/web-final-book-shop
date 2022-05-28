from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    about,
    cart,
    checkout,
    contact,
    main,
    product_detail,
    products,
)

urlpatterns = [
    path("season/<str:season>/", products, name="products"),
    path(
        "season/<str:season>/<int:id>/", product_detail, name="product_detail"
    ),
    path("", main, name="main"),
    path("contacts/", contact, name="contact"),
    path("about/", about, name="about"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
