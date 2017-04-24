from django.shortcuts import render
from .models import Product
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings


def all_products_bkp(request):
    pagetitle = "Products"
    subtitle = "Take a look into all products"
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products, "pagetitle": pagetitle, "subtitle": subtitle})

def all_products(request):
    pagetitle = "Products"
    subtitle = "Take a look into all products"
    products = Product.objects.all()

    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": 3.99,
        "currency": "USD",
        "item_name": "chocolate",
        "invoice": "%s-%s" % (5, uuid.uuid4()),
        "notify_url": settings.PAYPAL_NOTIFY_URL,
        "return_url": "%s/paypal-return" % settings.SITE_URL,
        "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    args = {"form": form, "products": products, "pagetitle": pagetitle, "subtitle": subtitle}
    return render(request, "products/products.html", args)

def __unicode__(self):
    return self.name