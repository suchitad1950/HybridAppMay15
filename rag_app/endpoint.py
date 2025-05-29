# import requests

# #url = "http://127.0.0.1:8000/ask/"
# url = "https://en.wikipedia.org/"  # Use this if running in a Docker container
# data = {
#     "query": "Albert Einstein",
#     "question": "What is Albert Einstein famous for?"
# }
# response = requests.post(url, json=data)
# print(response.json())


import requests

def get_wikipedia_data(query: str):
    # Wikipedia API endpoint
    url = "https://en.wikipedia.org/w/api.php"
    
    # Parameters for the API request
    params = {
        "action": "query",
        "format": "json",
        "titles": query,  # The page title to query
        "prop": "extracts",  # Get the content of the page
        "exintro": True,  # Only get the introduction section
        "explaintext": True  # Get plain text (no HTML)
    }
    
    # Make the GET request to the Wikipedia API
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage
query = "Albert Einstein key achivement in 100 words"
result = get_wikipedia_data(query)
print(result)

