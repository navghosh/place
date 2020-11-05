from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dests = Destination.objects.all()

    #dest1 = Destination()
    #dest1.name = "Delhi"
    #dest1.price = "500"
    #dest1.desc = "Capital Of India"
    #dest1.img = "destination1.jpg"

    #dest2 = Destination()
    #dest2.name = "Mumbai"
    #dest2.price = "800"
    #dest2.desc = "City that never sleeps"
    #dest2.img = "destination2.jpg"

    #dest3 = Destination()
    #dest3.name = "Bengaluru"
    #dest3.price = "600"
    #dest3.desc = "Tech City"
    #dest3.img = "destination3.jpg"

    #dests = [dest1,dest2,dest3]

    return render(request, "index.html", {'dests':dests})