from django.shortcuts import render

# Create your views here.
def home(request):

    import requests
    import json

     # pk_d6bfc8b1acda47ea906bdb7e6fe9ae4b

    #  create a request to pull data
    api_request = requests.get("https://api.iex.cloud/v1/data/core/quote/aapl?token=pk_d6bfc8b1acda47ea906bdb7e6fe9ae4b")

    # error handling to test whether connection success or not

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "This is not getting data"



    return render(request, 'home.html', {'api':api})


# view for about
def about(request):
    return render(request, 'about.html',{})