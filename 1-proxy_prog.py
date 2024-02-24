import socket

def main():
    # Establish connection with vg_recommender_ms (microservice)
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.connect(('localhost', 8888))

    # Send data to vg_recommender_ms (microservice)
    data = "['simulation', '10', ['Xbox', 'Playstation']]"
    proxy_socket.send(data.encode())

    # Receive result from vg_recommender_ms (microservice)
    result = proxy_socket.recv(1024).decode()
    print(result)

    # Close the connection
    proxy_socket.close()

if __name__ == "__main__":
    main()