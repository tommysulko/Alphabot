import socket
#                      IPv4             TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def main():
    s.connect(("192.168.0.130",5000))

    while True:
        msg = input("\nInserisci un messaggio per comandare il robot[comando|secondi]:")
        s.sendall(msg.encode())

if __name__ == "__main__":
    main()