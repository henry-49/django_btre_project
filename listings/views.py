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
    # query for search
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    # iexact means case insensitive 'i' | case sensitive will just be written as 'exact'
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    # iexact means case insensitive 'i' | case sensitive will just be written as 'exact'
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    # lte less than or equal to | <=
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    
    # Price
    # lte less than or equal to | <=
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # Creating dictonary
    context = {
         'state_choices' : state_choices,
         'bedroom_choices' : bedroom_choices,
         'price_choices' : price_choices,
         'listings' : queryset_list
    }
    return render(request, 'listings/search.html', context)