from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    #return HttpResponse("hello world")
    # dest1=Destination()
    # dest1.name="Mumbai"
    # dest1.desc="The city that never sleeps"
    # dest1.img = 'destination_1.jpg'
    # dest1.price=650
    # dest1.offer=False

    # dest2=Destination()
    # dest2.name="Bangaluru"
    # dest2.desc="Silicon valley of india"
    # dest2.img = 'destination_2.jpg'
    # dest2.price=750
    # dest2.offer=True

    # dest3=Destination()
    # dest3.name="Hyderabad"
    # dest3.desc="Land of Biryani"
    # dest3.img = 'destination_3.jpg'
    # dest3.price=700
    # dest3.offer=True

    # dests=[dest1, dest2, dest3]

    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})