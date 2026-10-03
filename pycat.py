#!/bin/python3

import argparse
import socket
import sys
from datetime import datetime

parser = argparse.ArgumentParser(description="A simple Python replacment for the tool Netcat")

parser.add_argument("-l", "--listen", action="store_true", help="listen")
parser.add_argument("-p", "--port", type=int, default=9999, help="specified port")
parser.add_argument("-t", "--target", default="0.0.0.0", help="specified IP")
parser.add_argument("-s", "--scan", action="store_true", help="port scanner")
args = parser.parse_args()

print(f"Target: {args.target}, Port: {args.port}, Listen: {args.listen}")
if args.port < 1 or args.port > 65535:
    print("[!] Invalid port number. Must be between 1 to 65535")

def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((args.target, args.port))
        
        if buffer:
            client.send(buffer.encode())
            
    except Exception as e:
                print(f"[!] Connection error: {e}")
    finally:
        client.close()
                
               
def port_scanner():
    target = socket.gethostbyname(args.target)
    
    print("-" * 50)
    print("Scanning Target... "+target)
    print("Time started "+str(datetime.now()))
    print("-" * 50)
    
    try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)       
            result = s.connect_ex((target,port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()
    
    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit()
    
    
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()         
                
if args.listen:
    server_loop()
    
elif args.scan:
    port_scanner()
    
else:
    buffer = input("Enter a message to send: ")
    client_sender(buffer)             
        
def server_loop():
    global target, port
    
    if not args.target:
        target = "0.0.0.0"
    else:
        target = args.target
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, args.port))
    server.listen(5)
    
    print(f"[*] listening on: {target}, {args.port}")
    
    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address:[0]}:{address:[1]}")
        
        request = client.recv(4096)
        print(request.decode())
        
        client.send(b"Hello from the server!")

        client.close()
        server.close() 

