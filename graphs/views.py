from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import StockForm
from .models import Stock


# Create your views here.
def home(request):

    import requests
    import json
    import urllib.parse

     # published_key = pk_d6bfc8b1acda47ea906bdb7e6fe9ae4b

    #  create a request to pull data
    api_request = requests.get("https://api.iex.cloud/v1/data/core/quote/aapl?token=pk_d6bfc8b1acda47ea906bdb7e6fe9ae4b")

    # error handling to test whether connection success or not
    # try:
    #     api = json.loads(api_request.content)

      
    # except Exception as e:
    #     api = "This is not getting data"

    # for search bar
    if request.method == 'POST':
        # ticker = ["AAPL", "AMZN","TSLA"] # replace with your ticker symbol
        ticker = request.POST['ticker']
        # encoded_ticker = urllib.parse.quote(ticker)

        api_request = requests.get(f"https://api.iex.cloud/v1/data/core/quote/{ticker}?token=pk_d6bfc8b1acda47ea906bdb7e6fe9ae4b")

        try:
            api = json.loads(api_request.content)

        # api = {}
        # for i in api:
        #     api.update(i)
        except Exception as e:
            api = "This is not getting data"
        
        return render(request, 'home.html', {'api':api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Company ticker in Search Stock"})


    

# dipslay view for about
def about(request):
    return render(request, 'about.html',{})

# function for creating stock page
def stock(request):

    import requests
    import json

    # to store Stock data
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():  # this is validation
            form.save()
            # popup message
            messages.success(request, ("New Stock has been added!"))
            return redirect('stock')
        
    else:

        # pulling data
        ticker = Stock.objects.all()

         # connecting to api
         
        return render(request, 'stock.html', {'ticker': ticker})
    

# create delete fucntion for stock
def deleteStock(request, stock_id):
    t = Stock.objects.get(pk=stock_id)  # called the id
    t.delete()
    messages.error(request, ("Stock has been deleted!"))
    return redirect('stock')


