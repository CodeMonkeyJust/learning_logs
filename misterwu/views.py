from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get("http://jsonplaceholder.typicode.com/users")
    api = json.loads(api_request.content)
    return render(request,'home.html',{"api":api})

def user(request):
    return render(request,'user.html',{})