import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    params = {
        "type": "single"  # Demander une blague courte
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("type") == "single":
            print("Joke: ", data.get("joke"))
        else:
            print("Joke setup: ", data.get("setup"))
            print("Joke delivery: ", data.get("delivery"))
    else:
        print(f"Error: Unable to retrieve joke (status code {response.status_code})")

if __name__ == "__main__":
    get_joke()
