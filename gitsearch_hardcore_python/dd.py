import requests

# Set the API endpoint and parameters
url = "https://api.github.com/search/repositories"
params = {
    # "q": "search query",  # replace with your search query
    "q": "mask detection in python",  # replace with your search query
    "sort": "stars",      # sort by number of stars
    "order": "desc",      # sort in descending order
}

# Make the request to the GitHub API
response = requests.get(url, params=params)

# Print the response content
print(response.json())




# import requests

# # Set the API endpoint and parameters
# url = "https://api.github.com/search/code"
# params = {
#     #"q": "search query",  # replace with your search query
#     "q": "mask detection in python", 
#     # "sort": "stars",      # sort by number of stars
#     # "order": "desc",      # sort in descending order
# }

# # Make the request to the GitHub API
# response = requests.get(url, params=params)

# # Print the response content
# print(response.json())
