from django.shortcuts import render

# Create your views here.
def home(request):

    import requests
    import json
    import urllib.parse

     # pk_d6bfc8b1acda47ea906bdb7e6fe9ae4b

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

def stock(request):
    return render(request, 'stock.html', {})