import socket

# WINNTER DETERMINATION FUNCTION
def determine_winner(num1, num2):
    # WINNER = HIGHER NUMBER WITH DIFFERENCE <=3 or LOWER NUMBER WITH DIFFERENCE > 3
    if num1==num2:
        # DRAW
        return 2
    elif abs(num1 - num2) <= 3:
        return 1 if num1 > num2 else 0
    else:
        return 0 if num1 < num2 else 1

# MAIN FUNCTION
def main():
    # TCP/IP SOCKET
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # BIND SOCKET TO IP/PORT
        s.bind(('localhost', 11111))
        # INCOMING CONNECTION/S MONITORING
        s.listen()
        # ACCEPT CONNECTION FROM CLIENT 1/PLAYER 1
        player1, _ = s.accept()
        # SAME, FROM FROM CLIENT 1/PLAYER 2
        player2, _ = s.accept()
        # RECEIVE NUMBERS AND DECODE FROM BYTES TO INTEGER
        num1 = int(player1.recv(1024).decode())
        num2 = int(player2.recv(1024).decode())

        # DETERMINE WINNER VIA FUNCTION ON TOP
        winner = determine_winner(num1, num2)

        # SEND RESPONSES TO CLIENTS
        if winner == 1:
            player1.sendall(str(1).encode())  # PLAYER 1 WINS
            player2.sendall(str(0).encode())  # PLAYER 2 LOSES
        elif winner == 0:
            player1.sendall(str(0).encode())  # PLAYER 1 LOSES
            player2.sendall(str(1).encode())  # PLAYER 2 WINS
        else:
            player1.sendall(str(2).encode())  # DRAW
            player2.sendall(str(2).encode())  # DRAW

# RUNNING FUNCTION
main()