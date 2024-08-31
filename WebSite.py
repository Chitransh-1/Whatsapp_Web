from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import filedialog
from datetime import datetime
import whtsap_function as fun

root = Tk()
root.state("zoomed")

def openfile():
    return filedialog.askopenfilename()

def dashboard():
    
    global framee_dashboard
    framee_dashboard = Frame(root, bg="white")
    framee_dashboard.place(x=0, y=0, height=1100, width=1990)
    framm = Frame(framee_dashboard, bg='lightblue', height=50, width=1950)
    framm.place(x=0, y=0)
    framm2 = Frame(framee_dashboard, bg='lightgrey', height=70, width=1950)
    framm2.place(x=270, y=50)
    framm3 = Frame(framee_dashboard, bg='lightgrey', height=600, width=850)
    framm3.place(x=270, y=200)
    framm4 = Frame(framee_dashboard, bg='yellow', height=675, width=750)
    framm4.place(x=1150, y=125)

    first_coloumn = ['Total', 'DELIVRD', 'EXPIRED', 'UNDELIV', 'REJECTED', 'SENT', 'UNKNOWN', 'PENDDING',]
    second_coloumn = ['0', '0', '0', '0', '0','0', '0', '0']
    treevieww = ttk.Treeview(framm4, columns=('Status', 'Value'), show= 'headings')
    treevieww.heading("Status", text="Status")
    treevieww.heading("Value", text="Value")
    for i in range(len(first_coloumn)):
        Status = first_coloumn[i]
        Value = second_coloumn[i]
        data = Status, Value
        treevieww.insert(parent="",index=0, values=data)
    treevieww.insert(parent="", index=0,values=("Total", "0"))
    treevieww.place(x=25, y=20, width=700, height=200)

    date = datetime.now()
    format_date = f"{date:%a, %b %d %Y}"
    w = Label(framee_dashboard, text=format_date, fg="white", bg="green", font=("helvetica", 15), relief="groove")
    w.place(x=350, y=150)

    credit_btnn7 = Button(framm2, text="Credit", background="lightblue", font=("Ariel", 11), relief="groove")
    credit_btnn7.place(x=20, y=17, width=100, height=40)
    w_api_btnn6 = Button(framm2, text="W-API:132", background="lightgreen", font=("Ariel", 11), relief="groove")
    w_api_btnn6.place(x=115, y=17, width=100, height=40)
    labell2 = Label(framm3, text="DELIVRD", bg="lightgrey")
    labell2.place(x=700, y=100)
    labell3 = Label(framm3, text="EXPIRED", bg="lightgrey")
    labell3.place(x=700, y=120)
    labell4 = Label(framm3, text="UNDELIV", bg="lightgrey")
    labell4.place(x=700, y=140)
    labell5 = Label(framm3, text="REJECTED", bg="lightgrey")
    labell5.place(x=700, y=160)
    labell6 = Label(framm3, text="SENT", bg="lightgrey")
    labell6.place(x=700, y=180)
    labell7 = Label(framm3, text="UNKNOWN", bg="lightgrey")
    labell7.place(x=700, y=200)
    labell8 = Label(framm3, text="PENDDING", bg="lightgrey")
    labell8.place(x=700, y=220)
    
    btn11 = Button(framm, text="Log Out", relief="groove", font=("Ariel", 11))
    btn11.place(x=1840, y=10)



def wapp_campaign():
    
    global framee_wapp
    framee_wapp = Frame(root, bg="white")
    framee_wapp.place(x=0, y=00, height=100, width=1650)
    
    logoutt = Frame(framee_wapp, bg='lightblue', height=50, width=1950)
    logoutt.place(x=0, y=0)
    wapp_mess = Frame(framee_wapp, bg="lightgrey", width=1950, height=50)
    wapp_mess.place(x=250, y=120)
    
    framm2 = Frame(framee_wapp, bg='white', height=70, width=1950)
    framm2.place(x=270, y=50)
    f2 = Text(framee_wapp, relief="groove", bg="lightgrey")
    f2.place(x=300, y=285, width=380, height=440)
    f3 = Text(framee_wapp, relief="groove", bg="lightgrey")
    f3.place(x=700, y=286,width=1080, height=150)
    f4 = Frame(framee_wapp, bg="lightblue",width=1080, height=40)
    f4.place(x=700, y=437)
    drg_drp_img_btn = Button(framee_wapp, text="""Drag & Drop image files(Maximum 4) or \nBrowse Image""", font=("Ariel", 13), bg="lightgrey", command=openfile, relief="groove")
    drg_drp_img_btn.place(x=700, y=478, width=1080, height=100)
    drg_drp_vid_btn = Button(framee_wapp, text="""Drag & Drop video files(Max size 1 MB)or Browse Video""", font=("Ariel", 13), bg="lightgrey", command=openfile, relief="groove")
    drg_drp_vid_btn.place(x=700, y=620, width=530, height=100)
    drg_drp_pdf_btn = Button(framee_wapp, text="""Drag & Drop PDF files(Max size 2 MB)or Browse PDF""", font=("Ariel", 13), bg="lightgrey", command=openfile, relief="groove")
    drg_drp_pdf_btn.place(x=1250, y=620, width=530, height=100)
    f6 = Frame(framee_wapp, bg="lightgreen",width=530, height=40)
    f6.place(x=700, y=579)
    f7 = Frame(framee_wapp, bg="lightblue",width=530, height=40)
    f7.place(x=1250, y=579)
    
    labell = Label(framm2, text="Credit", background="lightblue", width=10, height=2, font=("Ariel", 11), relief="groove")
    labell.place(x=20, y=17)
    credit_btnn5 = Button(framm2, text="Credit", background="lightblue", font=("Ariel", 11), relief="groove")
    credit_btnn5.place(x=20, y=17, width=100, height=40)
    w_api_btnn5 = Button(framm2, text="W-API:132", background="lightgreen", font=("Ariel", 11), relief="groove")
    w_api_btnn5.place(x=115, y=17, width=100, height=40)
    lbl1 = Label(framee_wapp, text="Campaign Name", font=("Ariel", 15), bg="lightgrey", relief="groove")
    lbl1.place(x=290, y=190, height=35, width=150)
    camp_entry = Entry(framee_wapp, relief="groove", bg="lightgreen", font=("Ariel", 16))
    camp_entry.place(x=440, y=190, height=35, width=510)
    
    lbl3 = Label(framee_wapp, text="Numbers:", font=("Ariel", 15), bg="white")
    lbl3.place(x=290, y=250)
    lbl4 = Label(framee_wapp, text="Message:", font=("Ariel", 15), bg="white")
    lbl4.place(x=700, y=250)
    lbl5 = Label(f4, text="Image Upload (Max File Size 3 MB.)", bg="lightblue", font=("Ariel", 10))
    lbl5.place(x=10, y=9)
    lbl6 = Label(f6, text="Video Upload (Max File Size 3 MB.)", bg="lightgreen", font=("Ariel", 10))
    lbl6.place(x=10, y=9)
    lbl7 = Label(f7, text="PDF (Max File Size 2 MB.)", bg="lightblue", font=("Ariel", 10))
    lbl7.place(x=10, y=9)
    btn11 = Button(logoutt, text="Log Out", relief="groove", font=("Ariel", 11))
    btn11.place(x=1840, y=10)
    btnn = Button(framee_wapp, text="Send Now", font=("Ariel", 14), bg="lightblue")
    btnn.place(x=300, y=800)

def button_Campaign():
    
    global btn_camp_frme
    btn_camp_frme = Frame(root, bg="white")
    btn_camp_frme.place(x=0, y=0, height=1100, width=1990)
    
    head_frm = Frame(btn_camp_frme, bg="lightblue")
    head_frm.place(x=0, y=0, height=50, width=2000)
    logout_btn = Button(head_frm, text="Log Out", bg="white", relief="groove", font=("Ariel", 11))
    logout_btn.place(x=1840, y=10)
    
    head1_frm = Frame(btn_camp_frme, bg="white", height=70, width=1950)
    head1_frm.place(x=270, y=50)
    credit_btnn4 = Button(head1_frm, text="Credit", background="lightblue", font=("Ariel", 11), relief="groove")
    credit_btnn4.place(x=20, y=17, width=100, height=40)
    w_api_btnn4 = Button(head1_frm, text="W-API:132", background="lightgreen", font=("Ariel", 11), relief="groove")
    w_api_btnn4.place(x=115, y=17, width=100, height=40)
    
    btn_camp_mess_frm = Frame(btn_camp_frme, bg="lightgrey", width=1950, height=50)
    btn_camp_mess_frm.place(x=250, y=120)
    txt_labell2 = Label(btn_camp_mess_frm, text="Button Campaign", font=("Ariel", 15), bg="lightgrey")
    txt_labell2.place(x=40, y=10)
    
    txt_labell3 = Label(btn_camp_frme, text="Campaign Name", font=("Ariel", 15), bg="lightgrey", relief="groove")
    txt_labell3.place(x=290, y=190, height=35, width=150)
    camp_entry = Entry(btn_camp_frme, relief="groove", bg="lightgreen", font=("Ariel", 16))
    camp_entry.place(x=440, y=190, height=35, width=510)
    
    txt_labell4 = Label(btn_camp_frme, text="Numbers:", font=("Ariel", 15), bg="white")
    txt_labell4.place(x=290, y=250)
    numb_txt = Text(btn_camp_frme, relief="groove", bg="lightgrey")
    numb_txt.place(x=300, y=285, width=380, height=550)
    
    txt_labell5 = Label(btn_camp_frme, text="Message:", font=("Ariel", 15), bg="white")
    txt_labell5.place(x=700, y=250)
    mess_txt = Text(btn_camp_frme, relief="groove", bg="lightgrey")
    mess_txt.place(x=700, y=286,width=1200, height=200)
    
    txt_labell6 = Label(btn_camp_frme, text="Link", font=("Ariel", 13), fg="white", bg="green", relief="groove")
    txt_labell6.place(x=700, y=500, height=30, width=40)
    link_entry = Entry(btn_camp_frme, relief="groove", bg="lightgrey", font=("Ariel", 13))
    link_entry.place(x=740,y=500,width=200, height=30)
    link_entry = Entry(btn_camp_frme, relief="groove", bg="lightgrey", font=("Ariel", 13))
    link_entry.place(x=940,y=500,width=960, height=30)
    
    txt_labell7 = Label(btn_camp_frme, text="Number", font=("Ariel", 13), fg="white", bg="blue", relief="groove")
    txt_labell7.place(x=700, y=550, height=30, width=75)
    number_entry = Entry(btn_camp_frme, relief="groove", bg="lightgrey", font=("Ariel", 13))
    number_entry.place(x=775,y=550,width=200, height=30)
    number_entry = Entry(btn_camp_frme, relief="groove", bg="lightgrey", font=("Ariel", 13))
    number_entry.place(x=975,y=550,width=925, height=30)
    
    img_frm = Frame(btn_camp_frme, bg="lightblue",width=1200, height=40)
    img_frm.place(x=700, y=600)
    txt_labell8 = Label(img_frm, text="Image Upload (Max File Size 1 MB.)", bg="lightblue", font=("Ariel", 10))
    txt_labell8.place(x=10, y=9)
    img_btn = Button(btn_camp_frme, text="""Drag & Drop image files(Maximum 4) or \nBrowse Image""""", relief="groove", bg="lightgreen", font=("Ariel", 12), command=openfile)
    img_btn.place(x=700, y=641, width=1200, height=100)
    
    vid_frm = Frame(btn_camp_frme, bg="lightgrey")
    vid_frm.place(x=700, y=750, width=590, height=40)
    txt_labell10 = Label(vid_frm, text="Video Upload (Max File Size 1 MB.)", bg="lightgrey", font=("Ariel", 11))
    txt_labell10.place(x=10, y=9)
    vid_btn = Button(btn_camp_frme, text="""Drag & Drop video files(Max size:3 MB)or Browse Video""", relief="groove", font=("Ariel", 13), bg="lightblue", command=openfile)
    vid_btn.place(x=700, y=790, width=590, height=100)
    
    vid_frm1 = Frame(btn_camp_frme, bg="lightgrey")
    vid_frm1.place(x=1312, y=750, width=590, height=40)
    txt_labell10 = Label(vid_frm1, text="PDF (Max File Size 2 MB.)", bg="lightgrey", font=("Ariel", 11))
    txt_labell10.place(x=10, y=9)
    pdf_btn = Button(btn_camp_frme, text="""Drag & Drop PDF files(Max size 2 MB)or Browse PDF""", relief="groove", font=("Ariel", 13), bg="lightblue", command=openfile)
    pdf_btn.place(x=1312, y=790, width=590, height=100)

def wapp_report():
    
    global wapp_report_frme
    wapp_report_frme = Frame(root, bg="lightgrey")
    wapp_report_frme.place(x=0, y=0, height=1100, width=1990)
    
    head_frm = Frame(wapp_report_frme, bg="lightblue")
    head_frm.place(x=0, y=0, height=50, width=2000)
    logout_btn = Button(head_frm, text="Log Out", bg="white", relief="groove", font=("Ariel", 11))
    logout_btn.place(x=1840, y=10)
    
    head1_frm = Frame(wapp_report_frme, bg="white", height=70, width=1950)
    head1_frm.place(x=270, y=50)
    credit_btnn3 = Button(head1_frm, text="Credit", background="lightblue", font=("Ariel", 11), relief="groove")
    credit_btnn3.place(x=20, y=17, width=100, height=40)
    w_api_btnn3 = Button(head1_frm, text="W-API:132", background="lightgreen", font=("Ariel", 11), relief="groove")
    w_api_btnn3.place(x=115, y=17, width=100, height=40)
    
    btn_camp_mess_frm = Frame(wapp_report_frme, bg="lightgrey", width=1950, height=50)
    btn_camp_mess_frm.place(x=250, y=120)
    txt_labell2 = Label(btn_camp_mess_frm, text="Whatsapp Report", font=("Ariel", 15), bg="lightgrey")
    txt_labell2.place(x=40, y=10)
    download_btn = Button(btn_camp_mess_frm, text="Download Report CSV", bg="lightblue", font=("Ariel", 10), relief="groove")
    download_btn.place(x=290, y=13, height=34, width=140)
    
    table_frm = Frame(wapp_report_frme, bg="white", height=300, width=1950)
    table_frm.place(x=250, y=190)
    show_labell = Label(table_frm, text="Show", font=("Ariel", 12), bg="white")
    show_labell.place(x=60, y=20)
    show_entry = Entry(table_frm, bg="lightgrey", font=("Ariel", 13), relief="groove")
    show_entry.place(x=105, y=20, height=25, width=50)
    entrie_labell = Label(table_frm, text="entries", font=("Ariel", 12), bg="white")
    entrie_labell.place(x=155, y=20)
    
    treevieww1 = ttk.Treeview(table_frm, columns=('Campname', 'Number', 'Message', 'Status', 'Submit Date', 'Download'), show= 'headings')
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure('Treeview', font=('Arial', 10))
    style.configure("Treeview.Heading", background="dark blue", font=('Arial', 12, 'bold'), foreground="light yellow")
    style.map('Treeview.Heading', background=[('active', 'blue')])
    
    treevieww1.heading("Campname", text="Campname")
    treevieww1.heading("Number", text="Number")
    treevieww1.heading("Message", text="Message")
    treevieww1.heading("Status", text="Status")
    treevieww1.heading("Submit Date", text="Submit Date")
    treevieww1.heading("Download", text="Download")
    
    coloumnss = []

    for i in range(len(coloumnss)):
        # Status = choice(first_coloumn)
        # Value = choice(second_coloumn)
        dataa = coloumnss
        data = dataa
        treevieww1.insert(parent="",index=0, values=data[i])
    treevieww1.place(x=60, y=60, width=1550, height=100)
    
    previous_btn = Button(table_frm, bg="white", text="Previous", relief="raised", font=("Areil", 12))
    previous_btn.place(x=1450, y=180)
    next_btn = Button(table_frm, bg="white", text="Next", relief="raised", font=("Areil", 12))
    next_btn.place(x=1530, y=180)
    

def register_wapp():
    global register_wapp_frme
    register_wapp_frme = Frame(root, bg="lightgrey")
    register_wapp_frme.place(x=0, y=0, height=1100, width=1990)
    
    head_frm = Frame(register_wapp_frme, bg="lightblue")
    head_frm.place(x=0, y=0, height=50, width=2000)
    logout_btn = Button(head_frm, text="Log Out", bg="white", relief="groove", font=("Ariel", 11))
    logout_btn.place(x=1840, y=10)
    
    head1_frm = Frame(register_wapp_frme, bg="white", height=70, width=1950)
    head1_frm.place(x=270, y=50)
    credit_btnn2 = Button(head1_frm, text="Credit", background="lightblue", font=("Ariel", 11), relief="groove")
    credit_btnn2.place(x=20, y=17, width=100, height=40)
    w_api_btnn2 = Button(head1_frm, text="W-API:132", background="lightgreen", font=("Ariel", 11), relief="groove")
    w_api_btnn2.place(x=115, y=17, width=100, height=40)
    
    btn_camp_mess_frm = Frame(register_wapp_frme, bg="lightgrey", width=1950, height=50)
    btn_camp_mess_frm.place(x=250, y=120)
    txt_labell2 = Label(btn_camp_mess_frm, text="Register WA", font=("Ariel", 15), bg="lightgrey")
    txt_labell2.place(x=40, y=10)
    
    identification_frm = Frame(register_wapp_frme, bg="white", width=1950, height=100)
    identification_frm.place(x=250, y=180)
    txt_label = Label(identification_frm, text="Identification Name:", font=("Ariel", 13), bg="white")
    txt_label.place(x=70, y=30)
    indenti_entry = Entry(identification_frm, bg="lightblue", relief="groove", font=("Ariel", 13))
    indenti_entry.place(x=229, y=30, width=230, height=30)
    register_btn = Button(identification_frm, text="Register & Scan", font=("Ariel", 10), bg="lightblue")
    register_btn.place(x=465, y=29, width=105, height=30)
    
    btn_camp_mess_frm = Frame(register_wapp_frme, bg="lightgrey", width=1950, height=50)
    btn_camp_mess_frm.place(x=250, y=120)
    txt_labell2 = Label(btn_camp_mess_frm, text="Whatsapp Report", font=("Ariel", 15), bg="lightgrey")
    txt_labell2.place(x=40, y=10)

def wapp_channel():
    global wapp_channel_frm
    wapp_channel_frm = Frame(root, bg="lightgrey")
    wapp_channel_frm.place(x=0, y=0, height=1100, width=1990)
    
    head_frm = Frame(wapp_channel_frm, bg="lightblue")
    head_frm.place(x=0, y=0, height=50, width=2000)
    logout_btn = Button(head_frm, text="Log Out", bg="white", relief="groove", font=("Ariel", 11))
    logout_btn.place(x=1840, y=10)
    
    head1_frm = Frame(wapp_channel_frm, bg="white", height=70, width=1950)
    head1_frm.place(x=270, y=50)
    credit_btnn1 = Button(head1_frm, text="Credit", background="lightblue", font=("Ariel", 11), relief="groove")
    credit_btnn1.place(x=20, y=17, width=100, height=40)
    w_api_btnn1 = Button(head1_frm, text="W-API:132", background="lightgreen", font=("Ariel", 11), relief="groove")
    w_api_btnn1.place(x=115, y=17, width=100, height=40)
    
    btn_camp_mess_frm = Frame(wapp_channel_frm, bg="lightgrey", width=1950, height=50)
    btn_camp_mess_frm.place(x=250, y=120)
    txt_labell2 = Label(btn_camp_mess_frm, text="WAPP Channel", font=("Ariel", 15), bg="lightgrey")
    txt_labell2.place(x=40, y=10)
    
    table_frm = Frame(wapp_channel_frm, bg="white", height=300, width=1950)
    table_frm.place(x=250, y=190)
    show_labell = Label(table_frm, text="Show", font=("Ariel", 12), bg="white")
    show_labell.place(x=60, y=20)
    show_entry = Entry(table_frm, bg="lightgrey", font=("Ariel", 13), relief="groove")
    show_entry.place(x=105, y=20, height=25, width=50)
    entrie_labell = Label(table_frm, text="entries", font=("Ariel", 12), bg="white")
    entrie_labell.place(x=155, y=20)
    search_labell = Label(table_frm, text="Search:", bg="white", font=("Ariel", 12))
    search_labell.place(x=1450, y=20)
    search_entry = Entry(table_frm, bg="lightblue", font=("Ariel", 12), relief="sunken")
    search_entry.place(x=1510, y=20, width=100, heigh=25)
    
    treevieww11 = ttk.Treeview(table_frm, columns=('Number', 'Name', 'Createdon', 'Status', 'Channel', 'Ping', 'Action'), show= 'headings')
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure('Treeview', font=('Arial', 10))
    style.configure("Treeview.Heading", background="dark blue", font=('Arial', 12, 'bold'), foreground="light yellow")
    style.map('Treeview.Heading', background=[('active', 'blue')])
    
    treevieww11.heading("Number", text="Number")
    treevieww11.heading("Name", text="Name")
    treevieww11.heading("Createdon", text="Createdon")
    treevieww11.heading("Status", text="Status")
    treevieww11.heading("Channel", text="Channel")
    treevieww11.heading("Ping", text="Ping")
    treevieww11.heading("Action", text="Action")
    
    coloumnss = []

    for i in range(len(coloumnss)):
        # Status = choice(first_coloumn)
        # Value = choice(second_coloumn)
        dataa = coloumnss
        treevieww11.insert(parent="",index=0, values=dataa[i])
    treevieww11.place(x=60, y=60, width=1550, height=100)
    
    previous_btn = Button(table_frm, bg="white", text="Previous", relief="raised", font=("Areil", 12))
    previous_btn.place(x=1450, y=180)
    next_btn = Button(table_frm, bg="white", text="Next", relief="raised", font=("Areil", 12))
    next_btn.place(x=1530, y=180)


def change_password():
    global change_password_frm
    change_password_frm = Frame(root, bg="lightgrey")
    change_password_frm.place(x=0, y=0, height=1100, width=1990)
    
    headd_frm = Frame(change_password_frm, bg="lightblue")
    headd_frm.place(x=0, y=0, height=50, width=2000)
    logout_btn = Button(headd_frm, text="Log Out", bg="white", relief="groove", font=("Ariel", 11))
    logout_btn.place(x=1840, y=10)
    
    headd1_frm = Frame(change_password_frm, bg="white", height=70, width=1950)
    headd1_frm.place(x=270, y=50)
    credit_btnn = Button(headd1_frm, text="Credit", background="lightblue", font=("Ariel", 11), relief="groove")
    credit_btnn.place(x=20, y=17, width=100, height=40)
    w_api_btnn = Button(headd1_frm, text="W-API:132", background="lightgreen", font=("Ariel", 11), relief="groove")
    w_api_btnn.place(x=115, y=17, width=100, height=40)
    
    btn_change_mess_frm = Frame(change_password_frm, bg="lightgrey", width=1950, height=50)
    btn_change_mess_frm.place(x=250, y=120)
    txt_labell22 = Label(btn_change_mess_frm, text="Change Password", font=("Ariel", 15), bg="lightgrey")
    txt_labell22.place(x=40, y=10)
    
    entries_frm = Frame(change_password_frm, bg="white", width=1950, height=400)
    entries_frm.place(x=250, y=180)
    current_pass_labell = Label(entries_frm, text="ENTER CURRENT PASSWORD", bg="white", font=("Ariel", 10))
    current_pass_labell.place(x=50, y=30)
    current_pass = Entry(entries_frm, show="*", font=("Ariel", 12), bg="lightblue", relief="groove")
    current_pass.place(x=50, y=52, height=35, width=450)
    new_pass_labell = Label(entries_frm, text="NEW PASSWORD", bg="white", font=("Ariel", 10))
    new_pass_labell.place(x=50, y=130)
    new_pass_entry = Entry(entries_frm, show="*", font=("Ariel", 12), bg="lightblue", relief="groove")
    new_pass_entry.place(x=50, y=152, height=35, width=450)
    conf_pass_labell = Label(entries_frm, text="CONFIRM PASSWORD", bg="white", font=("Ariel", 10))
    conf_pass_labell.place(x=50, y=240)
    conf_pass_entry = Entry(entries_frm, show="*", font=("Ariel", 12), bg="lightblue", relief="groove")
    conf_pass_entry.place(x=50, y=262, height=35, width=450)
    
    changee_pass_btn = Button(entries_frm, text="Change Password", relief="groove", bg="lightgreen", fg="black")
    changee_pass_btn.place(x=50, y=350, width=130, height=30)

def credit_history():
    global credit_history_frm
    credit_history_frm = Frame(root, bg="lightgrey")
    credit_history_frm.place(x=0, y=0, height=1100, width=1990)
    
    headd_frm11 = Frame(credit_history_frm, bg="lightblue")
    headd_frm11.place(x=0, y=0, height=50, width=2000)
    logout_btn11 = Button(headd_frm11, text="Log Out", bg="white", relief="groove", font=("Ariel", 11))
    logout_btn11.place(x=1840, y=10)
    
    headd12_frm = Frame(credit_history_frm, bg="white", height=70, width=1950)
    headd12_frm.place(x=270, y=50)
    credit_btnn7 = Button(headd12_frm, text="Credit", background="lightblue", font=("Ariel", 11), relief="groove")
    credit_btnn7.place(x=20, y=17, width=100, height=40)
    w_api_btnn8 = Button(headd12_frm, text="W-API:132", background="lightgreen", font=("Ariel", 11), relief="groove")
    w_api_btnn8.place(x=115, y=17, width=100, height=40)
    
    credit_hist_frm = Frame(credit_history_frm, bg="lightgrey", width=1950, height=50)
    credit_hist_frm.place(x=250, y=120)
    txt_labell22 = Label(credit_hist_frm, text="Credit Audit", font=("Ariel", 15), bg="lightgrey")
    txt_labell22.place(x=40, y=10)
    options = [
        "ALL", 
        "Credit/Debit", 
        "REFUND",
        "DEBIT",
        "CREDIT"
    ] 
    clicked = StringVar()  
    clicked.set( "Credit/Debit" )  
    drop = OptionMenu( credit_hist_frm , clicked , *options) 
    drop.place(x=560, y=17, width=300) 
    
    table_frm = Frame(credit_history_frm, bg="white", height=230, width=1950)
    table_frm.place(x=250, y=190)
    show_labell = Label(table_frm, text="Show", font=("Ariel", 12), bg="white")
    show_labell.place(x=60, y=20)
    show_entry = Entry(table_frm, bg="lightgrey", font=("Ariel", 13), relief="groove")
    show_entry.place(x=105, y=20, height=25, width=50)
    entrie_labell = Label(table_frm, text="entries", font=("Ariel", 12), bg="white")
    entrie_labell.place(x=155, y=20)
    search_labell = Label(table_frm, text="Search:", bg="white", font=("Ariel", 12))
    search_labell.place(x=1450, y=20)
    search_entry = Entry(table_frm, bg="lightblue", font=("Ariel", 12), relief="sunken")
    search_entry.place(x=1510, y=20, width=100, heigh=25)
    
    treevieww11 = ttk.Treeview(table_frm, columns=('UserName', 'ServiceName', 'Credit', 'Type', 'TermsTime', 'Old Credit', 'New Credit', 'sysnotes', 'Notes'))
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure('Treeview', font=('Arial', 10))
    style.configure("Treeview.Heading", background="dark blue", font=('Arial', 10, 'bold'), foreground="light yellow")
    style.map('Treeview.Heading', background=[('active', 'blue')])
    
    treevieww11.heading("#0", text="ID")
    treevieww11.heading("UserName", text="UserName")
    treevieww11.heading("ServiceName", text="ServiceName")
    treevieww11.heading("Credit", text="Credit")
    treevieww11.heading("Type", text="Type")
    treevieww11.heading("TermsTime", text="TermsTime")
    treevieww11.heading("Old Credit", text="Old Credit")
    treevieww11.heading("New Credit", text="New Credit")
    treevieww11.heading("sysnotes", text="sysnotes")
    treevieww11.heading("Notes", text="Notes")
    
    treevieww11.column("#0", width=30, stretch=NO)
    treevieww11.column("UserName", width=45)
    treevieww11.column("ServiceName", width=45)
    treevieww11.column("Credit", width=45)
    treevieww11.column("Type", width=45)
    treevieww11.column("TermsTime", width=45)
    treevieww11.column("Old Credit", width=45)
    treevieww11.column("New Credit", width=45)
    treevieww11.column("sysnotes", width=45)
    treevieww11.column("Notes", width=45)
    
    coloumnss = []

    for i in range(len(coloumnss)):
        # Status = choice(first_coloumn)
        # Value = choice(second_coloumn)
        dataa = coloumnss
        treevieww11.insert(parent="",index=0, values=dataa[i])
    treevieww11.place(x=35, y=60, width=1550, height=100)
    
    previous_btn = Button(table_frm, bg="white", text="Previous", relief="raised", font=("Areil", 12))
    previous_btn.place(x=1450, y=180)
    next_btn = Button(table_frm, bg="white", text="Next", relief="raised", font=("Areil", 12))
    next_btn.place(x=1530, y=180)



def manage_apikey():
    global manage_apikey_frm
    manage_apikey_frm = Frame(root, bg="lightgrey")
    manage_apikey_frm.place(x=0, y=0, height=1100, width=1990)
    
    headd_frm12 = Frame(manage_apikey_frm, bg="lightblue")
    headd_frm12.place(x=0, y=0, height=50, width=2000)
    logout_btn11 = Button(headd_frm12, text="Log Out", bg="white", relief="groove", font=("Ariel", 11))
    logout_btn11.place(x=1840, y=10)
    
    headd13_frm = Frame(manage_apikey_frm, bg="white", height=70, width=1950)
    headd13_frm.place(x=270, y=50)
    credit_btnn8 = Button(headd13_frm, text="Credit", background="lightblue", font=("Ariel", 11), relief="groove")
    credit_btnn8.place(x=20, y=17, width=100, height=40)
    w_api_btnn8 = Button(headd13_frm, text="W-API:132", background="lightgreen", font=("Ariel", 11), relief="groove")
    w_api_btnn8.place(x=115, y=17, width=100, height=40)
    
    gener_api_frm = Frame(manage_apikey_frm, bg="lightgrey", width=1950, height=50)
    gener_api_frm.place(x=250, y=120)
    txt_labell22 = Label(gener_api_frm, text="Generate API KEY", font=("Ariel", 10, "bold"), bg="lightgrey")
    txt_labell22.place(x=40, y=10)
    
    btn_frm = Frame( manage_apikey_frm, bg="white", width=1950, height=90)
    btn_frm.place(x=250, y=180)
    generate_btnn = Button(btn_frm, text="Generate New API KEY", font=("Ariel", 10, "bold"), bg="lightblue", relief="groove")
    generate_btnn.place(x=40, y=30)
    
    headd14_frm = Frame(manage_apikey_frm, bg="white", height=60, width=1950)
    headd14_frm.place(x=270, y=290)
    labell = Label(headd14_frm, text="Manage API KEY", font=("Ariel", 11), bg="white")
    labell.place(x=40, y=15)
    
    headd15_frm = Frame(manage_apikey_frm, bg="white", height=260, width=1950)
    headd15_frm.place(x=270, y=352)
    show_labell = Label(headd15_frm, text="Show", font=("Ariel", 12), bg="white")
    show_labell.place(x=35, y=15)
    show_entry = Entry(headd15_frm, bg="lightgrey", font=("Ariel", 13), relief="groove")
    show_entry.place(x=85, y=15, height=25, width=50)
    entrie_labell = Label(headd15_frm, text="entries", font=("Ariel", 12), bg="white")
    entrie_labell.place(x=140, y=15)
    search_labell = Label(headd15_frm, text="Search:", bg="white", font=("Ariel", 12))
    search_labell.place(x=1450, y=20)
    search_entry = Entry(headd15_frm, bg="lightblue", font=("Ariel", 12), relief="sunken")
    search_entry.place(x=1510, y=20, width=100, heigh=25)
    
    treevieww11 = ttk.Treeview(headd15_frm, columns=('Key', 'IP', 'Date', 'Action'), show= 'headings')
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure('Treeview', font=('Arial', 10))
    style.configure("Treeview.Heading", background="dark blue", font=('Arial', 10, 'bold'), foreground="light yellow")
    style.map('Treeview.Heading', background=[('active', 'blue')])
    
    treevieww11.heading("Key", text="Key")
    treevieww11.heading("IP", text="IP")
    treevieww11.heading("Date", text="Date")
    treevieww11.heading("Action", text="Action")
    
    coloumnss = []

    for i in range(len(coloumnss)):
        # Status = choice(first_coloumn)
        # Value = choice(second_coloumn)
        dataa = coloumnss
        treevieww11.insert(parent="",index=0, values=dataa[i])
    treevieww11.place(x=30, y=60, width=1550, height=100)
    
    previous_btn = Button(headd15_frm, bg="white", text="Previous", relief="raised", font=("Areil", 12))
    previous_btn.place(x=1450, y=180)
    next_btn = Button(headd15_frm, bg="white", text="Next", relief="raised", font=("Areil", 12))
    next_btn.place(x=1530, y=180)

def Chats():
    global chats_frm

    framm = Frame(root, bg='lightblue', height=50, width=1950)
    framm.place(x=0, y=0)
    btn11 = Button(framm, text="Log Out", relief="groove", font=("Ariel", 11))
    btn11.place(x=1840, y=10)
    
    # chats_frm = ctk.CTkFrame(root, fg_color="green", height=969, width=1990)
    # chats_frm.place(x=270, y=50)

    chats_frm = Frame(root, background="green")
    chats_frm.place(x=270, y=50, height=969, width=1990)

    numbers_frame = ctk.CTkFrame(chats_frm, height=966, width=400, fg_color="white")
    numbers_frame.place(x=0, y=0)
    number_scroll = ctk.CTkScrollableFrame(numbers_frame, height=799, width=372, fg_color="white")
    number_scroll.place(x=0, y=150)

    info_frame = ctk.CTkFrame(chats_frm, fg_color="white", corner_radius=0, height=59, width=1246)
    info_frame.place(x=401, y=0)

    scroll_frame = ctk.CTkScrollableFrame(chats_frm, fg_color="light yellow",height=776, width=1223)
    scroll_frame.place(x=402, y=60)

    chatt_frame = ctk.CTkFrame(chats_frm, fg_color="white", corner_radius=0, height=115, width=1246)
    chatt_frame.place(x=401, y=850)

    def insert_mess():
        deeta = textmess.get()
        fun.insert_msg(deeta, name_id, detee)
    send_bttn = ctk.CTkButton(chatt_frame, text="Send", font=("Arial", 16, "bold"), text_color="white", fg_color="darkgreen", corner_radius=5, command=insert_mess, width=50, height=40)
    send_bttn.place(x=1000, y=35)

    textmess = ctk.StringVar()
    text_entry = ctk.CTkEntry(chatt_frame, textvariable=textmess, fg_color="#99ff99", font=("Arial", 15), text_color="black", width=800, height=45)
    text_entry.place(x=150, y=35)

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
            label = ctk.CTkLabel(info_frame, text=namv, text_color="black", font=("Arial", 20, "bold"), width=100, height=30)
            label.place(x=10, y=10)
            label1 = ctk.CTkLabel(info_frame, text=mobv, text_color="black", font=("Arial", 20, "bold"), width=100, height=30)
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
                deta_frame.grid(row=yy, column=xx, pady=2, padx=70)
                
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
            box_frame.grid(row=y_position, column=0, padx=15, pady=3, sticky="nsew")  
            box_frame.bind("<ButtonRelease-1>", get_frame)
            boxxary.append(box_frame)

            id_label = ctk.CTkLabel(box_frame, text=idv, fg_color="#99ff99", font=('Arial', 14), text_color="black")
            id_label.grid(row=0, column=1, padx=60, pady=0, sticky="w")
            iddary.append(id_label)
            
            name_label = ctk.CTkLabel(box_frame, text=f"Name: {namev}", fg_color="#99ff99", font=('Arial', 17), text_color="black")
            name_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")
            nameeary.append(name_label)
            
            mobile_label = ctk.CTkLabel(box_frame, text=f"Mobile: {mobilev}", fg_color="#99ff99", font=('Arial', 19), text_color="black")
            mobile_label.grid(row=2, column=0, padx=10, pady=0, sticky="w")
            mobileeary.append(mobile_label)

            y_position += 1

    display_data_in_boxes()


Chats()
wapp_campaign()
button_Campaign()
wapp_report()
register_wapp()
wapp_channel()
credit_history()
change_password()
manage_apikey()
dashboard()



def dateBind(event):
    print("eventttt",event.widget)
    txtvv = event.widget["text"]
    txtv = event.widget["text"]
    print("You Select : ",txtv)

    if txtv == "Dashboard":
        framee_dashboard.place(x=0, y=0, height=1100, width=1990)
        framee_wapp.place_forget()
        btn_camp_frme.place_forget()
        register_wapp_frme.place_forget()
        wapp_report_frme.place_forget()
        wapp_channel_frm.place_forget()
        change_password_frm.place_forget()
        credit_history_frm.place_forget()
        manage_apikey_frm.place_forget()
    
    if txtv == "Wapp Campaign":
        framee_wapp.place(x=0, y=0, height=1100, width=1990)
        framee_dashboard.place_forget() 
        btn_camp_frme.place_forget()
        register_wapp_frme.place_forget()
        wapp_report_frme.place_forget()
        wapp_channel_frm.place_forget()
        change_password_frm.place_forget()
        credit_history_frm.place_forget()
        manage_apikey_frm.place_forget()
        
    if txtv == "Button Campaign":
        btn_camp_frme.place(x=0, y=0, height=1100, width=1990)
        framee_dashboard.place_forget()
        framee_wapp.place_forget()
        register_wapp_frme.place_forget()
        wapp_report_frme.place_forget()
        wapp_channel_frm.place_forget()
        change_password_frm.place_forget()
        credit_history_frm.place_forget()
        manage_apikey_frm.place_forget()
    
    if txtv == "WAPP Report":
        wapp_report_frme.place(x=0, y=0, height=1100, width=1990)
        framee_dashboard.place_forget()
        framee_wapp.place_forget()
        btn_camp_frme.place_forget()
        register_wapp_frme.place_forget()
        wapp_channel_frm.place_forget()
        change_password_frm.place_forget()
        credit_history_frm.place_forget()
        manage_apikey_frm.place_forget()
    
    if txtv == "Register WAPP":
        register_wapp_frme.place(x=0, y=0, height=1100, width=1990)
        framee_dashboard.place_forget()
        framee_wapp.place_forget()
        btn_camp_frme.place_forget()
        wapp_report_frme.place_forget() 
        wapp_channel_frm.place_forget()
        change_password_frm.place_forget()
        credit_history_frm.place_forget()
        manage_apikey_frm.place_forget()
    
    if txtv == "Wapp Channel":
        wapp_channel_frm.place(x=0, y=0, height=1100, width=1990)
        framee_dashboard.place_forget()
        framee_wapp.place_forget()
        btn_camp_frme.place_forget()
        wapp_report_frme.place_forget() 
        register_wapp_frme.place_forget()
        change_password_frm.place_forget()
        credit_history_frm.place_forget()
        manage_apikey_frm.place_forget()
    
    if txtv == "Change Password":
        change_password_frm.place(x=0, y=0, height=1100, width=1990)
        framee_dashboard.place_forget()
        framee_wapp.place_forget()
        btn_camp_frme.place_forget()
        wapp_report_frme.place_forget() 
        register_wapp_frme.place_forget()
        wapp_channel_frm.place_forget()
        credit_history_frm.place_forget()
        manage_apikey_frm.place_forget()
    
    if txtv == "Credit History":
        credit_history_frm.place(x=0, y=0, height=1100, width=1990)
        framee_dashboard.place_forget()
        framee_wapp.place_forget()
        btn_camp_frme.place_forget()
        wapp_report_frme.place_forget() 
        register_wapp_frme.place_forget()
        wapp_channel_frm.place_forget()
        change_password_frm.place_forget()
        manage_apikey_frm.place_forget()
    
    if txtv == "Manage APIKey":
        manage_apikey_frm.place(x=0, y=0, height=1100, width=1990)
        framee_dashboard.place_forget()
        framee_wapp.place_forget()
        btn_camp_frme.place_forget()
        wapp_report_frme.place_forget() 
        register_wapp_frme.place_forget()
        wapp_channel_frm.place_forget()
        change_password_frm.place_forget()
        credit_history_frm.place_forget()
    
    if txtv == "Chats":
        chats_frm.place(x=270, y=50, height=969, width=1990)
        # chats_frm.place(x=270, y=50)
        framee_dashboard.place_forget()
        framee_wapp.place_forget()
        btn_camp_frme.place_forget()
        wapp_report_frme.place_forget() 
        register_wapp_frme.place_forget()
        wapp_channel_frm.place_forget()
        change_password_frm.place_forget()
        credit_history_frm.place_forget()
        manage_apikey_frm.place_forget()


# framm1 = ctk.CTkFrame(root, fg_color='darkgreen', height=968, width=270)
# framm1.place(y=50)
# framm1.grid_propagate(False)

framm1 = Frame(root, background='darkgreen')
framm1.place(y=50, height=968, width=270)

buttonsV = ["Dashboard", "Wapp Campaign", "Button Campaign", "WAPP Report", "Register WAPP", "Wapp Channel","Manage User", "Credit Manage", "Credit History", "Change Password", "Manage APIKey", "Logout", "Chats"]
yy = 10
for i in range(len(buttonsV)):
    tttt = buttonsV[i].lower()

    # btn =  ctk.CTkButton(framm1, text=buttonsV[i], width=180, fg_color="white", text_color="green", hover_color="lightblue", font=("Arial", 12, "bold"))
    # btn.grid(row =i, column = 0, padx= 40, pady=13)

    btn = Button(framm1, text=buttonsV[i], width=15)
    btn.place(x=55, y=yy*6)

    #btn.place(x=70, y=yy*6)
    yy += 10
    
    btn.bind("<Button-1>", dateBind)

root.mainloop()