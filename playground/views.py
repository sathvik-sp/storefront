from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def sayHello(request):
    #return HttpResponse("hello world")
    return render(request,'hello.html', {'name':'Sathvik'})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num1'])
    res=val1+val2
    return render(request,'result.html',{'result':res})