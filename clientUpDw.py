import socket

HOST = '127.0.0.1' 
PORT = 65432
choice = input("Enter what do you want, download or upload a file: ").lower()
if choice == "upload":
    path = input("To upload, please provide the path of your file: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        request = choice + "|" + path
        s.sendall(request.encode('utf-8'))
        data = s.recv(1024)
elif choice == "download": 
    path = input("To download, please provide the file name: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        request = choice + "|" + path
        s.sendall(request.encode('utf-8'))
        data = s.recv(1024)
else:
    print("Invalid choice")
    data = None

if data:
    print(data.decode('utf-8'))
