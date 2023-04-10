import requests

# Set the API endpoint and parameters
url = "https://api.github.com/search/repositories"
params = {
    #"q": "search query",
    "q": "mask detection in java", 
    "sort": "stars",
    "order": "desc",
}

# Make the request to the GitHub API
response = requests.get(url, params=params)

# Parse the JSON response and store repositories in a list
repositories = response.json()["items"]

# Print the repository names and URLs in a horizontal table
print("Repository Names\tRepository URLs")
print("---------------\t---------------")
for repo in repositories:
    print(f"{repo['name']}\t\t{repo['html_url']}")
