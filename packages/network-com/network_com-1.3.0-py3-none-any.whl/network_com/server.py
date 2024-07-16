# network_com/server.py

import socket
from time import sleep
import threading
from concurrent.futures import ThreadPoolExecutor
import ssl
from .config import MAX_THREADS, TCP_PORT, UDP_PORT

def send_ip():
    broadcast_ip = socket.gethostbyname(socket.gethostname()).rsplit('.', 1)[0] + ".255"
    msg = b'response'
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while True:
        try:
            udp_socket.sendto(msg, (broadcast_ip, UDP_PORT))
            sleep(1)
        except Exception as e:
            print(f"Error broadcasting IP: {e}")

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")
    client_socket.settimeout(60)  # Set timeout for client socket
    try:
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    print(f"Client {client_address} disconnected")
                    break
                msg = data.decode()
                print(f"Received from {client_address}: {msg}")
                client_socket.send("h".encode())
            except socket.timeout:
                print(f"Client {client_address} timed out")
                break
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"Connection with {client_address} closed")

def tcp_server(certfile, keyfile):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", TCP_PORT))
    server_socket.listen()
    print(f"TCP server listening on port {TCP_PORT}")

    # Wrap the socket with SSL
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    server_socket = context.wrap_socket(server_socket, server_side=True)

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        while True:
            try:
                client_socket, client_address = server_socket.accept()
                executor.submit(handle_client, client_socket, client_address)
            except Exception as e:
                print(f"Error accepting connections: {e}")

def main(certfile, keyfile):
    udp_thread = threading.Thread(target=send_ip)
    tcp_thread = threading.Thread(target=tcp_server, args=(certfile, keyfile))
    udp_thread.start()
    tcp_thread.start()
    udp_thread.join()
    tcp_thread.join()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run network server.")
    parser.add_argument('--certfile', required=True, help="Path to the SSL certificate file")
    parser.add_argument('--keyfile', required=True, help="Path to the SSL key file")
    args = parser.parse_args()
    main(args.certfile, args.keyfile)
