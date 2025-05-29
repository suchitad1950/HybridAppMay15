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

def get_wikipedia_data(query: str, word_limit: int):
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
        data = response.json()
        pages = data.get("query", {}).get("pages", {})
        page = next(iter(pages.values()))  # Get the first page
        if "missing" in page:
            print(f"Page '{query}' does not exist on Wikipedia.")
            return None
        content = page.get("extract", "")
        
        # Limit the number of words in the result
        limited_content = " ".join(content.split()[:word_limit])
        return limited_content
    else:
        print(f"Error: {response.status_code}")
        return None    

# Example usage
query = "Albert Einstein "
result = get_wikipedia_data(query, word_limit=100 )
print(result)

