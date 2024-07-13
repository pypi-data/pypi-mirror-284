import socket

def scan(host, port):
    """
    Check if a port is open on a given host.

    :param host: The hostname or IP address to check.
    :param port: The port number to check.
    :return: A string indicating if the port is open or closed.
    """
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for the connection attempt

    try:
        # Try to connect to the host and port
        result = sock.connect_ex((host, port))
        if result == 0:
            return f"Port {port} on {host} is open."
        else:
            return f"Port {port} on {host} is closed."
    except socket.error as e:
        return f"Error occurred: {e}"
    finally:
        # Close the socket
        sock.close()