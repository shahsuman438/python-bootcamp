from django.shortcuts import render
from django.http import HttpResponse
from .models import homepagemodel
# from .models import homepagemodel
# Create your views here.


def homepage(request):
    # data = {
    #     "firstName": "suman",
    #     "lastName": "sah",
    #     "email": "abc@gmail.com"
    # }
    obj1 = homepagemodel()
    obj1.firstName = "user1"
    obj1.lastName = "user1last"
    obj1.email = "user1@gmail.com"
    obj1.isAdmin = True

    obj2 = homepagemodel()
    obj2.firstName = "user2"
    obj2.lastName = "user2last"
    obj2.email = "user2@gmail.com"
    obj2.isAdmin = False

    obj3 = homepagemodel()
    obj3.firstName = "user3"
    obj3.lastName = "user3last"
    obj3.email = "user3@gmail.com"
    obj3.isAdmin = True
    data = [obj1, obj2, obj3]
    return render(request, 'homes.html', {'data': data})

# def homepage(request):
#     dest1 = homepagemodel()
#     dest1.name = "mumbai"
#     dest1.desc = 'city of dreams'
#     return render(request, 'home.html', {'dest1': dest1})


# def add(request):
#     # val1 = int(request.GET['num1'])
#     # val2 = int(request.GET['num2'])
#     val1 = int(request.POST['num1'])
#     val2 = int(request.POST['num2'])
#     return render(request, 'result.html', {'result': val1+val2})
