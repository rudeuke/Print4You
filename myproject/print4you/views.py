from django.shortcuts import redirect, render
from django.http import HttpResponse
from print4you.models import Printout
from print4you.forms import PrintoutForm


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
    context = {'form': form, 'price': priceString, 'imagePath': imagePath}
    return render(request, 'calculator.html', context)
