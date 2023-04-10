import requests

# Set the API endpoint and parameters
url = "https://api.github.com/search/repositories"
params = {
    #"q": "search query",  # replace with your search query
    "q": "mask detection in php",  # replace with your search query
    "sort": "stars",      # sort by number of stars
    "order": "desc",      # sort in descending order
}

# Make the request to the GitHub API
response = requests.get(url, params=params)

# Parse the JSON response and print the repository names and URLs
repositories = response.json()["items"]
for repo in repositories:
    print(repo["name"], repo["html_url"])
