import socket

# MAIN FUNCTION
def main():
    # USER INPUT
    num = int(input("Enter an integer number between 0 and 9: "))
    # TCP/IP SOCKET
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # CONNECT TO SERVER (IP/PORT)
        s.connect(('localhost', 11111))
        # NUMBER > SERVER
        s.sendall(str(num).encode())
        # RESPONSE (RECEIVE & DECODE FROM BYTES TO INTEGER)
        response = s.recv(1024).decode()
        # PRINT RESULT, BASED ON RESPONSE
        print("You win!" if response == '1' else "You lose!" if response == '0' else "Draw!")

# RUNNING FUNCTION
main()