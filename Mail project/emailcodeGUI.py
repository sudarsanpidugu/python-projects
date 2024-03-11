import smtplib
import time
import schedule
import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox

def send_email():
    email = sender_email.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    message = message_entry.get("1.0", tk.END)

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, "tzdt wqrg gptr gdcz")
    server.sendmail(email, receiver_email, text)
    print(f"Email has been sent to {receiver_email}")
    messagebox.showinfo("Success", "Email has been sent successfully!")

    messagebox
    server.quit()

def schedule_email():
    if messagebox.showinfo("Success", "Email has been Schedule successfully!"):
        # delivery_date = date_entry.get()
        delivery_time = time_entry.get()
        # datetime_str = f"{delivery_date} {delivery_time}"
        # schedule.every().day.at(datetime_str).do(send_email)
        schedule.every().day.at(delivery_time).do(send_email)

        # Keep the script running
        while True:
            schedule.run_pending()
            time.sleep(1)

# GUI Setup
root = tk.Tk()
img=PhotoImage(file='Mail.png')
root.iconphoto(False,img)
root.resizable(False,False)
root.title("Smart Mail")
root.geometry('850x600')

titlehead =tk.Label(root,text='Welcome to Smart Mail',bd=4, bg='skyblue',fg='white', font=('Comic Sans MS',15,'bold'))
titlehead.pack(fill='x',side='top')

bgimg = PhotoImage(file='mail3.png')
imglable = Label(image=bgimg)
imglable.pack(fill=X)

# sender
sender_label = tk.Label(root,text="Your Email:",fg='white', bg="#1e81b0",font=('',12,'bold'))
sender_label.place(x=30, y=70)

sender_email = tk.Entry(root,bg="#B0BEC5",fg="black",font=('calbery',13))
sender_email.place(x=30, y=105,width=300 , height=30)

# receiver
receiver_lable = tk.Label(root,text="Receiver Email:",fg='white', bg="#1e81b0",font=('',12,'bold'))
receiver_lable.place(x=30, y=150)

receiver_entry =tk.Entry(root,bg="#B0BEC5",fg="black",font=('calbery',13))
receiver_entry.place(x=30, y=185,width=300, height=30)

#Subject
subject_label = tk.Label(root,text="Subject:",fg='white', bg="#1e81b0",font=('',12,'bold'))
subject_label.place(x=30, y=230)

subject_entry = tk.Entry(root,bg="#B0BEC5",fg="black",font=('calbery',10))
subject_entry.place(x=30, y=265,width=300, height=30)

# Message
message_label = tk.Label(root,text="Message:",fg='white', bg="#1e81b0",font=('',12,'bold'))
message_label.place(x=30, y=310)

message_entry = tk.Text(root,height=5, width=42,bg="#B0BEC5",fg="black",font=('calbery',10))
message_entry.place(x=30, y=345)

# Date
date_label = tk.Label(root, text="Date (YYYY-MM-DD):", fg='white', bg="#1e81b0", font=('', 10, 'bold'))
date_label.place(x=30, y=440)

date_entry = tk.Entry(root, bg="#B0BEC5", fg="black", font=('caliber', 10))
date_entry.place(x=30, y=475, width=160, height=30)

# Time
time_label = tk.Label(root,text="Time (HH:MM):",fg='white', bg="#1e81b0",font=('',10,'bold'))
time_label.place(x=210, y=440)

time_entry = tk.Entry(root,bg="#B0BEC5",fg="black",font=('calbery',10))
time_entry.place(x=210, y=475,width=120, height=30)



# ===================  Buttons ==================================

send_button = tk.Button(root, command=send_email,text="Send Now",bg="#81C784",fg='white', font=('Comic Sans MS',12,'bold'),relief=GROOVE)
send_button.place(x=60, y=515,width=80)

schedule_button = tk.Button(root, command=schedule_email,text="Schedule",bg='#AB47BC',fg='white', font=('Comic Sans MS',12,'bold'),relief=GROOVE,)
schedule_button.place(x=170, y=515,width=80)

root.mainloop()
