from django.shortcuts import render

# Create your views here.

from datetime import datetime, timedelta
def home(request):
    response = render(request, 'home.html')
    data = {
        'age': 19,
        "name":"Morsalin",

    }
    # response.set_cookie("name", "Morsalin", max_age = 10) # it sets cookies second wise
    # response.set_cookie("data", data, expires = datetime.utcnow()+timedelta(days=10))
    response.set_cookie("data", data)

    return response


def getCookie(request):
    data = request.COOKIES.get('data')  # eita ekta string return korba jeta ka dictionary hisaba peta amake evaluate korta hoiba
    print("before evaluate", type(data)) # it is a string
    data = eval(data)

    print("after evaluate", type(data)) # now it is a  dictionary

    return render(request, 'get.html',{'data': data})


def deleteCookie(request):
    response = render(request, 'del.html')
    response.delete_cookie("name")
    return response
