import socket
import ast

# Dictionary of games data
games = [
    {"genre": "rpg", "title": "Final Fantasy XVI", "cost": "70", "length": "35", "platform": ["Playstation"], "image_name": "ffxvi.jpg"},
    {"genre": "rpg", "title": "Xenoblade Chronicles 3", "cost": "60", "length": "3", "platform": ["Nintendo Switch"], "image_name": "xbc.jpg"},
    {"genre": "rpg", "title": "Final Fantasy VII Ever Crisis", "cost": "0", "length": "45", "platform": ["Mobile", "PC"], "image_name": "ffvii.jpg"},
    {"genre": "action-adventure", "title": "Red Dead Redemption 2", "cost": "60", "length": "50", "platform": ["Playstation", "Xbox", "PC"], "image_name": "rdr2.jpg"},
    {"genre": "action-adventure", "title": "The Legend of Zelda: Tears of the Kingdom", "cost": "70", "length": "60", "platform": ["Nintendo Switch"], "image_name": "totk.jpg"},
    {"genre": "action-adventure", "title": "Marvel's Spider-Man 2", "cost": "70", "length": "20", "platform": ["Playstation"], "image_name": "sm2.jpg"},
    {"genre": "adventure", "title": "Twisted Wonderland", "cost": "Free", "length":"100+", "platform": ["Mobile"], "image_name": "twst.jpg"},
    {"genre": "adventure", "title": "Kingdom Hearts III", "cost": "60", "length": "30", "platform": ["Playstation", "Xbox", "Nintendo Switch", "PC"], "image_name": "kh3.jpg"},
    {"genre": "adventure", "title": "Stray", "cost": "30", "length": "5", "platform": ["Playstation", "Xbox", "PC"], "image_name": "stray.jpg"},
    {"genre": "simulation", "title": "Stardew Valley", "cost": "15", "length": "100+", "platform": ["Nintendo Switch", "Playstation", "Xbox", "PC", "Mobile"], "image_name": "stardew.jpg"},
    {"genre": "simulation", "title": "Animal Crossing: New Horizons", "cost": "60", "length": "100+", "platform": ["Nintendo Switch"], "image_name": "anch.jpg"},
    {"genre": "simulation", "title": "Dredge", "cost": "25", "length": "10", "platform": ["Nintendo Switch", "Playstation", "Xbox", "PC"], "image_name": "dredge.jpg"},
    {"genre": "platform", "title": "Cuphead", "cost": "25", "length": "25", "platform": ["Nintendo Switch", "Playstation", "Xbox", "PC"], "image_name": "cuphead.jpg"},
    {"genre": "platform", "title": "Super Mario Odyssey", "cost": "60", "length": "15", "platform": ["Nintendo Switch"], "image_name": "mario.jpg"},
    {"genre": "platform", "title": "Sonic Mania", "cost": "20", "length": "5", "platform": ["Nintendo Switch", "Playstation", "Xbox", "PC"], "image_name": "sonic.jpg"}
]

# Algorithm to recommend game based on input (a list in string form)
def show_game_info(input):
    for game in games:
        if game['genre'] == input[0] and game['length'] == input[1]:
            for platform in input[2]:
                if platform in game['platform']:
                    return [game["title"], game["length"], game["length"], game["platform"], game["image_name"]]
            return "No Match Found"
    return "No Match Found"

# Main function to communicate with proxy_prog
def main():
    # Setup socket for communication with proxy_prog
    sum_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sum_socket.bind(('localhost', 8888))
    sum_socket.listen(1)

    print("Ready to receive connections...")

    while True:
        # Accept connection
        conn, addr = sum_socket.accept()
        print("Connected by", addr)

        # Receive data from proxy_prog
        data = conn.recv(1024).decode()
        print("Data received:", data)

        # Convert received string to list, run show_game_info function, store return in result
        input = ast.literal_eval(data)
        result = show_game_info(input)

        # Send result back to proxy_prog as string
        conn.send(str(result).encode())

        # Close connection
        conn.close()

if __name__ == "__main__":
    main()