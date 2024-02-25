# cs361_vg_recommender_ms
This microservice waits for a call from the videogame recommender web app. The call must pass a string that contains genre, length, and platform(s) selected by the web app. The microservice will then return a string of a list of videogame title, cost, length, platform, and image name. Any code in this read.me is assumed to be in Python.

Connection to the microservice can be achieved by using Flask.

# Calling and sending data to this microservice can be modeled after this code:
    # function to send data and request data back from microservice
    def send_string_to_microservice(string_of_preference):
        url = "http://localhost:5001/display_game"
        payload = {"input_string": string_of_preference}
        response = requests.post(url, json=payload)
        return response

    # calls send_string_to_microservice function
    response = send_string_to_microservice(string_of_preference)

Note that the data sent to this microservice needs to be a string of a list. In the list are 3 elements with the following data and in order of: GENRE, LENGTH, and LIST OF PLATFORM(S). GENRE and LENGTH are strings. LIST OF PLATFORM(S) is a list.

# Receiving result from the microservice can be modeled after this code:
    # function to receive data from microservice
    def receive_data_from_microservice(response):
        recommended_game = response.json()["recommended_game"]
        return recommended_game

    # calls receive_data_from_microservice function
    game_recommendation = receive_data_from_microservice(response)

Note that the data received from this microservice will be a string of a list. In the list are 5 elements with following the data and in order of: VIDEOGAME TITLE, COST, LENGTH, LIST OF PLATFORM(S), and IMAGE NAME. VIDEOGAME TITLE, COST, LENGTH, and IMAGE NAME are strings. LIST OF PLATFORM(S) is a list.

See below for an example code to establish connection, to call/send data to the microservice, and to receive data from the microservices.

# Sample code to connect, call, receive from this microservice
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
