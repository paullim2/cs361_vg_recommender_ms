import requests

# string holds data from web app submission
string_of_preference = "['rpg', '35', ['Xbox', 'Playstation']]"

# function to send data and request data back from microservice
def send_string_to_microservice(string_of_preference):
    url = "http://localhost:5001/display_game"
    payload = {"input_string": string_of_preference}
    response = requests.post(url, json=payload)
    return response

# calls send_string_to_microservice function
response = send_string_to_microservice(string_of_preference)

# function to receive data from microservice
def receive_data_from_microservice(response):
    recommended_game = response.json()["recommended_game"]
    return recommended_game

# calls receive_data_from_microservice function
game_recommendation = receive_data_from_microservice(response)

# prints recommended game and its details
print(game_recommendation)