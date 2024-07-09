import socket
import os
import shutil

# 1 - Set up a listening socket
HOST = '127.0.0.1' 
PORT = 65432

def handle_client(conn):
    try:
        data = conn.recv(1024)
        if not data:
            return
        print(f"Received data: {data}")  # מדפיס את הנתונים שהתקבלו

        directory = "DataBaseFiles"
        parent_dir = r"C:\Users\ACER\OneDrive - fun flex ltd\משפחה\יהלי כהן\מועדון מתכנתים\Python projects\Upload_Download_Files"
        path = os.path.join(parent_dir, directory)
        mode = 0o666
        if not os.path.exists(path):
            try:
                if not os.path.exists(parent_dir):
                    print(f"Parent directory does not exist: {parent_dir}")
                else:
                    os.makedirs(path, mode=mode, exist_ok=True)
                    print(f"Directory '{directory}' created successfully at '{path}'")
            except PermissionError:
                print(f"Permission denied: unable to create directory at '{path}'")
            except OSError as error:
                print(f"Error creating directory '{directory}' at '{path}': {error}")

        decoded_data = data.decode('utf-8')  # מפענח את הנתונים חזרה למחרוזת
        request, string2 = decoded_data.split("|")

        if request.lower() == "upload":
            shutil.copy(string2, path)
            conn.sendall(b"Upload complete")
        elif request.lower() == "download":
            file_name = os.path.join(path, string2)
            if os.path.exists(file_name):
                download_folder = os.path.expanduser("~") + "\\Downloads\\"
                shutil.copy(file_name, download_folder)
                conn.sendall(b"Download complete")
            else:
                conn.sendall(b"File doesn't exist in our DB")
    except ConnectionResetError as e:
        print(f"Connection reset by peer: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        try:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                handle_client(conn)
                break
        except Exception as e:
            print(f"Failed to accept connection: {e}")
    s.close()
    print("Server closed")
