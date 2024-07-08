from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    #return HttpResponse("hello world")
    dest1=Destination()
    dest1.name="Mumbai"
    dest1.desc="The city that never sleeps"
    dest1.price=800

    dest2=Destination()
    dest2.name="Delhi"
    dest2.desc="The capital city of India"
    dest2.price=1800
    
    return render(request,'index.html',{'dest1':dest1,'dest2':dest2})