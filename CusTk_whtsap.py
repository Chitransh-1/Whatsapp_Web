import customtkinter as ctk
from tkinter import *
from datetime import datetime
import whtsap_function as fun

root = ctk.CTk()
root.title("WhatsApp Web")
root.geometry("1200x800")

sidebar_frame = ctk.CTkFrame(root, height=1100, width=110, fg_color="darkgreen", corner_radius=0)
sidebar_frame.place(x=0, y=0)

numbers_frame = ctk.CTkFrame(root, height=1100, width=400, fg_color="white", corner_radius=0)
numbers_frame.place(x=110, y=0)
number_scroll = ctk.CTkScrollableFrame(numbers_frame, height=850, width=372, fg_color="white")
number_scroll.place(x=0, y=150)

info_frame = ctk.CTkFrame(root, fg_color="white", corner_radius=0, height=59, width=1410)
info_frame.place(x=510, y=0)

scroll_frame = ctk.CTkScrollableFrame(root, fg_color="light yellow",height=827, width=1382)
scroll_frame.place(x=512, y=60)

message_frame = ctk.CTkFrame(root, fg_color="white", corner_radius=0, height=117, width=1410)
message_frame.place(x=510, y=900)

def insert_mess():
    deeta = textmess.get()
    fun.insert_msg(deeta, name_id, detee)
send_bttn = ctk.CTkButton(message_frame, text="Send", font=("Arial", 10, "bold"), text_color="white", fg_color="darkgreen", corner_radius=5, command=insert_mess, width=50, height=40)
send_bttn.place(x=1300, y=35)

textmess = ctk.StringVar()
text_entry = ctk.CTkEntry(message_frame, textvariable=textmess, fg_color="#99ff99", font=("Arial", 15), text_color="black", width=1000, height=45)
text_entry.place(x=250, y=35)

def get_frame(event):
    global listtList, entName, entryNoo, name_id
    listtList = []
    widgetV = str(event.widget)

    widgetVV = widgetV.split("!")
    lennnn = len(widgetVV)-1
    widwid = widgetVV[lennnn-1]

    entName = widwid
    nono = widwid.replace("ctkframe", "")
    nono = nono.replace(".", "")

    if nono.isdigit():
        entryNoo = int(nono) - 1
    else:
        entryNoo = 0

    name_id = iddary[entryNoo].cget('text')
    
    get_name = fun.get_name(name_id)
    for namee in get_name:
        namv = namee[0]
        mobv = namee[1]
        label = ctk.CTkLabel(info_frame, text=namv, text_color="black", font=("Arial", 16, "bold"), width=100, height=30)
        label.place(x=10, y=10)
        label1 = ctk.CTkLabel(info_frame, text=mobv, text_color="black", font=("Arial", 16, "bold"), width=100, height=30)
        label1.place(x=120, y=10)
    
    def convert_date(date_input):
        try:
            if date_input is None:
                return "N/A"
            if isinstance(date_input, datetime):
                date_obj = date_input
            else:
                date_obj = datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S')
            return date_obj.strftime('%d-%m-%y %H:%M')
        except ValueError:
            return date_input
    
    idid = iddary[entryNoo].cget('text')
    msgg7_data = fun.get_msgg(idid)
    y_position = 1
    for widget in scroll_frame.winfo_children():
        widget.destroy()

    if msgg7_data:
        yy = 1
        for deta in msgg7_data:
            global detee
            msg1 = ""
            msg2 = ""
            xx = 0
            if deta[8] == 'rec':
                msg2 = deta[2]
                xx = 2
            if deta[8] == 'sn':
                msg1 = deta[2]
                xx = 600
            detee = deta[5]
            dete = convert_date(deta[5])
            
            messa = deta[2]

            length = len(messa.split('\n'))
            hh = length * 20
            deta_frame = ctk.CTkFrame(scroll_frame, fg_color="#99ff99",  corner_radius=5, height=hh + 30, width=410)
            deta_frame.grid(row=yy, column=xx, pady=2, padx=150)
            
            mess_sn_label = ctk.CTkLabel(deta_frame, text=messa, fg_color="#99ff99", text_color="black", font=("Arial", 20), height=hh)
            mess_sn_label.place(x=3, y=0)

            data_label = ctk.CTkLabel(deta_frame, text=dete, fg_color="#99ff99", text_color="black", font=("Arial", 12))
            data_label.place(x=280, y=hh)
            yy += 1
            y_position += 40
            
        scroll_frame.update_idletasks()
        scroll_frame._parent_canvas.yview_moveto(1.0)
    else:
        print("No messages found for the selected ID")

def display_data_in_boxes():
    global iddary, nameeary, mobileeary
    detaa = fun.get_detaa()
    y_position = 5

    labell = ctk.CTkLabel(numbers_frame, text="Chats", font=("Arial", 20, 'bold'), fg_color="white", text_color="black")
    labell.place(x=20, y=7)

    search_entry = ctk.CTkEntry(numbers_frame, fg_color="lightgrey", text_color="black", font=("Arial", 15), width=350, height=30)
    search_entry.place(x=20, y=45)

    btton = ctk.CTkButton(numbers_frame, text="All", fg_color="lightgrey", text_color="black", width=50)
    btton.place(x=20, y=95)
    btton1 = ctk.CTkButton(numbers_frame, text="Group", fg_color="lightgrey", text_color="black", width=50)
    btton1.place(x=120, y=95)
    btton2 = ctk.CTkButton(numbers_frame, text="Add", fg_color="lightgrey", text_color="black", width=50)
    btton2.place(x=220, y=95)
    btton3 = ctk.CTkButton(numbers_frame, text="Delete", fg_color="lightgrey", text_color="black", width=50)
    btton3.place(x=320, y=95)

    boxxary = []
    iddary = []
    nameeary = []
    mobileeary = []
    
    for row in detaa:
        idv = row[0]
        namev = row[1]
        mobilev = row[2]
        
        box_frame = ctk.CTkFrame(number_scroll, fg_color="#99ff99",height=50, width=100)
        box_frame.grid(row=y_position, column=0, padx=15, pady=3, sticky="nsew")  # Adjust column and sticky
        
        box_frame.bind("<ButtonRelease-1>", get_frame)
        boxxary.append(box_frame)

        id_label = ctk.CTkLabel(box_frame, text=idv, fg_color="#99ff99", font=('Arial', 14), text_color="black")
        id_label.grid(row=0, column=1, padx=60, pady=0, sticky="w")  # Align to the left
        iddary.append(id_label)
        
        name_label = ctk.CTkLabel(box_frame, text=f"Name: {namev}", fg_color="#99ff99", font=('Arial', 14), text_color="black")
        name_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")
        nameeary.append(name_label)
        
        mobile_label = ctk.CTkLabel(box_frame, text=f"Mobile: {mobilev}", fg_color="#99ff99", font=('Arial', 18), text_color="black")
        mobile_label.grid(row=2, column=0, padx=10, pady=0, sticky="w")
        mobileeary.append(mobile_label)

        y_position += 1

display_data_in_boxes()

btn = ctk.CTkButton(root, text="click", command=display_data_in_boxes, fg_color="grey", text_color="yellow", width=20)
btn.place(x=10, y=30)
root.mainloop()