from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

def index(request):
     # Fetching data from the database
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

     # Creating dictonary
    context = {
         'listings' : listings
     } 

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP 
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    # Creating dictonary
    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }

    return render(request, 'pages/about.html', context)