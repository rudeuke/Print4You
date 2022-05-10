from django.shortcuts import render
from django.http import HttpResponse
from print4you.forms import PrintoutForm


def index(request):
    return HttpResponse("hello world")


def calculator(request):
    form = PrintoutForm()
    if request.method == 'POST':
        form = PrintoutForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'calculator.html', context)
