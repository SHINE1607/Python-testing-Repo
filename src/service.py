import requests 

database = {
    1: "Alice", 
    2: "Bob", 
    3: "Janice", 
    4: "Chandler", 
}

def get_user_from_database(user_id):
    return database.get(user_id)

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError 