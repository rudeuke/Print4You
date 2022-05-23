from django.shortcuts import redirect, render
from django.http import HttpResponse
from print4you.models import Printout, Order
from print4you.forms import PrintoutForm, OrderForm, AddressForm


def index(request):
    return HttpResponse("hello world")


def calculator(request):
    form = PrintoutForm()
    if request.method == 'POST':
        form = PrintoutForm(request.POST, request.FILES,)
        if form.is_valid():
            printout = form.save()
            return redirect('update_printout', pk=printout.pk)

    context = {'form': form}
    return render(request, 'calculator.html', context)


def updatePrintout(request, pk):
    printout = Printout.objects.get(id=pk)
    form = PrintoutForm(instance=printout)
    if request.method == 'POST':
        form = PrintoutForm(request.POST, request.FILES, instance=printout)
        if form.is_valid():
            printout.price = None
            form.save()
            return redirect('update_printout', pk=printout.pk)
    priceString = f"Cena: {printout.price} zł"
    imagePath = printout.image_file.url
    context = {'form': form, 'price': priceString,
               'imagePath': imagePath, 'printout': printout}
    return render(request, 'calculator.html', context)


def newOrder(request, pk):
    printout = Printout.objects.get(id=pk)
    orderForm = OrderForm()
    addressForm = AddressForm()
    address = None
    currentUser = None

    if request.method == 'GET':
        if request.user.is_authenticated and not request.user.is_staff:
            currentUser = request.user
            address = currentUser.address
            address.pk = None
            address.user = None
            addressForm = AddressForm(instance=address)

    if request.method == 'POST':
        addressForm = AddressForm(request.POST)
        if addressForm.is_valid():
            address = addressForm.save()

        order = Order(printout=printout, cost=0,
                      address=address, user=currentUser)
        orderForm = OrderForm(request.POST, instance=order)
        if orderForm.is_valid():
            order = orderForm.save()
            return redirect('/')

    context = {'orderForm': orderForm, 'addressForm': addressForm}
    return render(request, 'order.html', context)
