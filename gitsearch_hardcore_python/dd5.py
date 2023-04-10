import requests

# Set the API endpoint and parameters
url = "https://api.github.com/search/repositories"
params = {
    #"q": "search query",
    "q": "mask detection in python", 
    "sort": "stars",
    "order": "desc",
}

# Make the request to the GitHub API
response = requests.get(url, params=params)

# Parse the JSON response and store repositories in a list
repositories = response.json()["items"]

# Print the repository names in a table
print("Repository Names:")
print("-----------------")
for repo in repositories:
    print(repo["name"])

# Print the repository URLs in a table
print("\nRepository URLs:")
print("-----------------")
for repo in repositories:
    print(repo["html_url"])
