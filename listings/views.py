from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from .choices import price_choices, bedroom_choices, state_choices
from django.http import HttpResponse
from .models import Listing
from .models import Realtor



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
    # Get listing or displays 404 page
    listing = get_object_or_404(Listing, pk=listing_id)

    
    # Creating dictonary
    context = {
        'listing' : listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    # Creating dictonary
    context = {
         'state_choices' : state_choices,
         'bedroom_choices' : bedroom_choices,
         'price_choices' : price_choices
    }
    return render(request, 'listings/search.html', context)