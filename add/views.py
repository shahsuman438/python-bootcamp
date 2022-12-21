from django.shortcuts import render

# Create your views here.


def add(request):
    return render(request, 'add.html')


def result(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1+num2
    return render(request, 'result.html', {'result': result})
