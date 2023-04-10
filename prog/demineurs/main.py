#!/usr/bin/env python3
import socket
import re

HOST = "newbiecontest.org"  # The server's hostname or IP address
PORT = 10001  # The port used by the server
N_MINES = 0
# STATUS =

def recvall(sock, max_msg_size=1024):
    # message = []
    string_lines = ""
    print("📩 Received: ")
    while True:
        bytes_line = sock.recv(max_msg_size)
        # no data
        if not bytes_line:
            break
        # data
        string_lines += (bytes_line.decode('utf-8'))
        # print(bytes_line)
        if b"Indiquer la position d'un mine\n>:" in bytes_line:
            break
        if b"Votre case (sous la forme \"x,y\") : " in bytes_line:
            break
        # Perdu : Il y avait une mine ici
    print(string_lines)

    if "+--" in string_lines:
        p = re.compile(r'-\+\n([| 0-9?\n]+)\+-') # get body
        BODY = p.findall(string_lines)
        # print("🐥BODY")
        # print(BODY[0])
        print("🐔LINES")
        LINES = BODY[0].split("\n")
        for line in LINES:
            print(line)

    # for bytes_line in bytes_line:
    #     string_line = bytes_line.decode('utf-8')
    #     string_lines += string_line
    #     if "Vous devez trouver" in string_line:
    #         p = re.compile(r'trouver (\d+) mines')
    #         N_MINES = p.findall(string_line)[0]
    #     if "Indiquer la position" in string_line:
    #         break
    #     if "Votre case (sous" in string_line:
    #         break
    # get board
    # if "+--" in string_lines:
        # p = re.compile(r'(\+-+\+)\s')
        # p = re.compile(r'-\+\n([| 0-9?\n]+)\+-') # get body
        # BODY = p.findall(string_lines)
        # print("BODY")
        # print(BODY[0])
        # print("LINES")
        # print("\n".split(BODY[0]))
    # print
    # print("📩 Received: "+string_lines)

def send(sock, bytes):
    s.sendall(bytes)
    print("⬆️ Sent: "+str(bytes))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = recvall(s) # receive board & get N_MINES
    # for i in [1,2,3]:
    send(s, b'1') # send 1-test
    data = recvall(s)
    send(s, b'0,0') # send x,y
    data = recvall(s) # receive board


    send(s, b'1') # send 1-test
    data = recvall(s)
    send(s, b'5,5') # send x,y
    data = recvall(s) # receive board
