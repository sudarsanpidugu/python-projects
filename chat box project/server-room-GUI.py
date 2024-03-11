import socket
from tkinter import*
import tkinter as tk
from threading import Thread
# import cv2

def receive_messages():
    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                chat_box.config(state=tk.NORMAL)
                chat_box.insert(tk.END, f"{client}: {message}\n")
                chat_box.config(state=tk.DISABLED)
                chat_box.see(tk.END)
        except ConnectionAbortedError:
            break

def send_message(event=None):
    message = message_entry.get()
    if message:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"Me: {message}\n")
        chat_box.config(state=tk.DISABLED)
        chat_box.see(tk.END)
        conn.send(message.encode())
        message_entry.delete(0, tk.END)



# Define a function to handle emoji selection and sending
def send_emoji(emoji):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"Me: {emoji}\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)
    conn.send(emoji.encode())

# Create a GUI window with a selection of emojis
def show_emojis():
    emoji_window = tk.Toplevel(root)
    emoji_window.title("Select Emoji")
    
    emojis = ["😊", "😂", "😍", "😎", "👍", "👏", "🎉", "❤️", "😁", "😃"]
    
    for emoji in emojis:
        emoji_button = tk.Button(emoji_window, text=emoji, font=("Arial", 12), command=lambda e=emoji: send_emoji(e))
        emoji_button.pack(pady=5)


def send_photo():
    pass

def send_document():
    pass

def on_closing():
    conn.close()
    root.quit()

def connect_to_client():
    global conn, client
    conn, address = new_socket.accept()
    client = conn.recv(1024).decode()
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"Connection established with {client}\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)
    send_message_button.config(state=tk.NORMAL)
    
    receive_thread = Thread(target=receive_messages)
    receive_thread.daemon = True
    receive_thread.start()




# GUI setup
root = tk.Tk()
img=PhotoImage(file='whatsaplogo.png')
root.iconphoto(False,img)
root.resizable(False,False)
root.title("Smart Chat Box")

root.geometry('450x600')
titlehead =tk.Label(root,text='Welcome to Your Chat', bd=4, bg='#009973', fg='white', font=('Comic Sans MS',15,'bold'))
titlehead.pack(fill='x',side='top')

chat_frame = tk.Frame(root, bg='#009973', bd=5,)
chat_frame.place(x=0,y=45, width=450, height=550)

chat_frame = tk.Frame(root)
chat_frame.pack(padx=10, pady=15)

scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_box = tk.Text(chat_frame, height=20 ,width=45, background='white', font='blue',state=tk.DISABLED, yscrollcommand=scrollbar.set)
chat_box.pack()

message_entry = tk.Entry(root,width=30,font='25')
message_entry.place(x=40,y=530, height=30)

# camera_img = PhotoImage(file='C:\\Users\\pidug\\Desktop\\Internship\\chat-room\\chatroom-GUI - Copy\\camera.png')
# camera_button = tk.Button(root, image=camera_img, bg='#009973', bd=0, command=send_photo)
# camera_button.place(x=385, y=3)

# document_img = PhotoImage(file='C:\\Users\\pidug\\Desktop\\Internship\\chat-room\\chatroom-GUI - Copy\\Document.png')
# documentsent = tk.Button(root, image=document_img, bg='#009973', bd=0, command=send_document)
# documentsent.place(x=320, y=525)

emoji_img = PhotoImage(file='emoji.png')
emoji_button = tk.Button(root, image=emoji_img, bg='#009973', bd=0, command=show_emojis)
emoji_button.place(x=5, y=525)

send_logo_img = PhotoImage(file='send1.png')
send_message_button = tk.Button(root, image=send_logo_img, bg='#009973', bd=0, command=send_message)
send_message_button.place(x=390, y=520)


root.protocol("WM_DELETE_WINDOW", on_closing)

# Networking setup--
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
server_ip = socket.gethostbyname(host)
port = 1060
new_socket.bind((host, port))
print('Binding successful!')
print("This is your IP: ", server_ip)
name = input('Enter name: ')
new_socket.listen(1)

connect_to_client()

root.mainloop()



# socket.socket(): A function that creates and returns a new socket object.
# socket.gethostname(): A function that returns the hostname of the current machine.
# socket.gethostbyname(): A function that returns the IPv4 address of a given hostname.
# socket.getaddrinfo(): A function that returns a list of information about a socket address, such as the family, type, protocol, and canonical name.
# socket.AF_INET: A constant that represents the address family for IPv4 sockets.
# socket.AF_INET6: A constant that represents the address family for IPv6 sockets.
# socket.SOCK_STREAM: A constant that represents the socket type for TCP sockets.
# socket.SOCK_DGRAM: A constant that represents the socket type for UDP sockets.
# socket.error: An exception that is raised for socket-related errors.
# socket.timeout: An exception that is raised when a socket operation times out.
