import socket
from inputimeout import inputimeout, TimeoutOccurred
import ssl
from .config import TCP_PORT, UDP_PORT

def tcpp(addr, certfile):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with SSL
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    # context.verify_mode = ssl.CERT_NONE
    context.load_verify_locations(certfile)
    client_socket = context.wrap_socket(client_socket)

    try:
        client_socket.connect((addr[0], TCP_PORT))
        print(f"Connected to server at {addr[0]}:{TCP_PORT}")
        client_socket.settimeout(60)  # Set timeout for client socket
        while True:
            try:
                data = inputimeout(prompt='', timeout=5)
                client_socket.send(data.encode())
            except TimeoutOccurred:
                continue
            except Exception as e:
                print(f"Error sending data: {e}")
                break
    except Exception as e:
        print(f"Error connecting to server: {e}")
    finally:
        client_socket.close()
        print("Connection closed, waiting for new server broadcast")

def udp_listener(certfile):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_socket.bind(("0.0.0.0", UDP_PORT))
    print(f"Listening for server broadcast on port {UDP_PORT}")
    while True:
        try:
            data, addr = udp_socket.recvfrom(1024)
            if data == b'response':
                tcpp(addr, certfile)
        except Exception as e:
            print(f"Error receiving UDP broadcast: {e}")

def main(certfile):
    udp_listener(certfile)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run network client.")
    parser.add_argument('--certfile', required=True, help="Path to the SSL certificate file")
    args = parser.parse_args()
    main(args.certfile)
