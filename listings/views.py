from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing



# Create your views here.
def index(request):
    # Fetching data from the database
    listings = Listing.objects.all()

    # Creating dictonary
    context = {
        'listings' : listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')