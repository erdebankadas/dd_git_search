from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from .models import *

def repository_list(request):
    if request.method == "POST":
        search_query = request.POST.get("search_query")
        url = "https://api.github.com/search/repositories"
        params = {
            "q": search_query, 
            "sort": "stars",
            "order": "desc",
        }
        response = requests.get(url, params=params)
        repositories = response.json()["items"]

        # Add repository URLs to each repository dictionary
        for repo in repositories:
            repo["url"] = repo["html_url"]
    else:
        repositories = []
    
    return render(request, "repository_list.html", {"repositories": repositories})

