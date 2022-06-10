from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")

        print('name: ', name)
        print('amount: ', amount)

    return render(request, "index.html")


def success(request):
    return render(request, "success.html")
