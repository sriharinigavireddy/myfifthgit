from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'hari'}
    return render(request,'jinja_print.html',context=d)


def user(request):
    d={'name':'ram','age':21}
    return render(request,'user.html',context=d)