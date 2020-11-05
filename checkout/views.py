from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents
from membership.models import Membership
from .models import Order

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        basket = request.session.get('basket', {})
        for item_id, quantity in basket.items():
            membership = get_object_or_404(Membership, pk=item_id)
            pid = request.POST.get('client_secret').split('_secret')[0]
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe.PaymentIntent.modify(pid, metadata={
                'basket': json.dumps(request.session.get('basket', {})),
                'save_info': request.POST.get('save_info'),
                'username': request.user,
                'membership': membership,
            })
            return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment cannot be \
            processed at the moment, please try agaon later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        for item_id, quantity in basket.items():
            membership = get_object_or_404(Membership, pk=item_id)

            form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'street_address1': request.POST['street_address1'],
                'street_address2': request.POST['street_address2'],
                'town_or_city': request.POST['town_or_city'],
                'postcode': request.POST['postcode'],
                'country': request.POST['country'],
            }
            order_form = OrderForm(form_data)
            if order_form.is_valid():
                order = order_form.save(commit=False)
                order.membership = membership
                order.save()

                request.session['save_info'] = 'save-info' in request.POST
                return redirect(reverse(
                    'checkout_success', args=[order.order_number]))
            else:
                messages.error(request, 'There was an error with your form. \
                    Please double check your information')

    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request,
                           "There's nothing in your basket at the moment")
            return redirect('membership')

        current_basket = basket_contents(request)
        total = current_basket['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it on your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ Handle successful checkouts """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed. \
        Your order number is {order_number}. A confirmation \
            email has been sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
