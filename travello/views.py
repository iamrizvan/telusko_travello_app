from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 749
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Gujrat'
    dest2.desc = 'The heritage of India'
    dest2.img = 'destination_2.jpg'
    dest2.price = 669
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Delhi'
    dest3.desc = 'The city of Mughals'
    dest3.img = 'destination_3.jpg'
    dest3.price = 559
    dest3.offer = True

    dest4 = Destination()
    dest4.name = 'Laddakh'
    dest4.desc = 'Explore the beauty of while hills'
    dest4.img = 'destination_4.jpg'
    dest4.price = 899
    dest4.offer = False

    dests = [dest1,dest2,dest3,dest4]

    return render(request,"index.html",{'dests':dests})
