from django.shortcuts import render, redirect
from django.views.generic.base import View
import stripe
from order.models import Order, OrderItem
from django.views import View
from django.conf import settings
from cart.models import Cart

# Create your views here.


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def get(self, request,  *args, **kwargs):
        cart = Cart.objects.get(
            order_id__customer_id=request.user)
        order = OrderItem.objects.filter(order=cart.order).all()

        items = [qs for qs in order]
        line_items = []

        for item in items:
            line_items.append(
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(item.product.price) * 100,
                        "product_data": {
                            "name": item.product.title,
                            "description": item.product.description,
                            "images": [
                                f"{settings.BACKEND_DOMAIN}/{item.product.image}"
                            ],
                        },
                    },
                    "quantity": item.quantity,
                }
            )

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://127.0.0.1:8000/checkout/success",
            cancel_url="http://127.0.0.1:8000",
        )
        return redirect(checkout_session.url)


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(customer=request.user, completed=False)
        order.completed = True
        order.save()
        cart = Cart.objects.get(order_id__customer_id=request.user).delete()
        return render(request, "success.html")
