from django.shortcuts import render
from .models import Product
from paypal.standard.forms import PayPalPaymentsForm


def all_products(request):
    pagetitle = "Products"
    subtitle = "Take a look into all products"
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products, "pagetitle": pagetitle, "subtitle": subtitle})

@property
def paypal_form(self):
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": self.price,
        "currency": "USD",
        "item_name": self.name,
        "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
        "notify_url": settings.PAYPAL_NOTIFY_URL,
        "return_url": "%s/paypal-return" % settings.SITE_URL,
        "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
    }
    return PayPalPaymentsForm(initial=paypal_dict)

def __unicode__(self):
    return self.name

# Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)    