from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing



# Create your views here.
def index(request):
    # Fetching data from the database
    # listings = Listing.objects.all()
    # oder by -list_date desc and filter is_published=True shows when is true
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    #Using Paginator displays limit of 6 pages
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    # Creating dictonary
    context = {
        'listings' : page_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')