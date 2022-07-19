from django.shortcuts import render
import razorpay

from django.views.decorators.csrf import csrf_exempt

from razorpay_second.settings import (Raz_Public_Key, Raz_Secret_Key)

from .models import Coffee

# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount")) * 100
        client = razorpay.Client(auth=(Raz_Public_Key, Raz_Secret_Key))
        payment = client.order.create(
            {
                'amount': amount,
                'currency': 'INR',
                'payment_capture': '1'
            }
        )
        print('payment: ', payment)

        coffee = Coffee(name=name, amount=amount, payment_id=payment['id'])
        coffee.save()
        return render(request, "index.html", {'payment': payment})

    return render(request, "index.html")

@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        print('a: ', a)
    return render(request, "success.html")
