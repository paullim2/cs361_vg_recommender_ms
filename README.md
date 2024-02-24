# cs361_vg_recommender_ms
This microservice waits for a call from the videogame recommender web app. The call must pass a string that contains genre, length, and platform(s) selected by the web app. The microservice will then return a string of a list of videogame title, cost, length, platform, and image name. Any code in this read.me is assumed to be in Python.

Connection to the microservice can be achieved by using socket.

Calling and sending data to this microservice can be accomplished by this code:
# To call and send data to vg_recommender_ms (microservice)
    data = "['GENRE', 'LENGTH', ['LIST OF PLATFORM(S)']]"
    proxy_socket.send(data.encode())

Note that the data sent to this microservice needs to be a string of a list. In the list are 3 elements with the following data and in order of: genre, length, and list of platform(s). GENRE and LENGTH are strings. LIST OF PLATFORM(S) is a list.

Receiving result from the microservice can be accomplished by this code:
# To receive result from vg_recommender_ms (microservice)
    result = proxy_socket.recv(1024).decode()
    print(result)

Note that the data received from this microservice will be a string of a list. In the list are 5 elements with following the data and order in order of: VIDEOGAME TITLE, COST, LENGTH, LIST OF PLATFORM(S), and IMAGE NAME. VIDEOGAME TITLE, COST, LENGTH, and IMAGE NAME are strings. LIST OF PLATFORM(S) is a list.

See below for an example code to establish connection, to call/send data to the microservice, and to receive data from the microservices.

# Sample code to connect, call, receive from this microservice
    import socket
    
    def main():
        # Establish connection with vg_recommender_ms (microservice)
        proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxy_socket.connect(('localhost', 8888))
    
        # To call and send data to vg_recommender_ms (microservice)
        data = "['simulation', '10', ['Xbox', 'Playstation']]"
        proxy_socket.send(data.encode())
    
        # To receive result from vg_recommender_ms (microservice)
        result = proxy_socket.recv(1024).decode()
        print(result)
    
        # Close the connection
        proxy_socket.close()
    
    if __name__ == "__main__":
        main()
