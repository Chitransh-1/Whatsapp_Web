from tkinter import *
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
from datetime import datetime

# Initialize the main application window
root = Tk()
root.title("Create Database and Table")
root.geometry("250x250")

def delete_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        if conn.is_connected():
            mycursor = conn.cursor()
            myquery = "DROP DATABASE vardhmann"
            mycursor.execute(myquery)
            messagebox.showinfo("Success", "Database 'vardhmann' DROP successfully.")
    except Error as e:
        messagebox.showerror("Error", f"Error DROP database: {e}")
    finally:
        # Check if 'mycursor' and 'conn' exist and if the connection is open
        if 'mycursor' in locals():
            mycursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

def create_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        if conn.is_connected():
            mycursor = conn.cursor()
            myquery = "CREATE DATABASE IF NOT EXISTS vardhmann"
            mycursor.execute(myquery)
            messagebox.showinfo("Success", "Database 'vardhmann' created successfully.")
    except Error as e:
        messagebox.showerror("Error", f"Error creating database: {e}")
    finally:
        # Check if 'mycursor' and 'conn' exist and if the connection is open
        if 'mycursor' in locals():
            mycursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

def create_table():
    try:
        # Connect to MySQL server and specify the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="vardhmann"
        )
        if conn.is_connected():
            mycursor = conn.cursor()

            # First table creation query
            myquery1 = """
            CREATE TABLE IF NOT EXISTS msgg (
                ID INT(6) AUTO_INCREMENT PRIMARY KEY NOT NULL,
                idn INT(6),
                msg VARCHAR(250),
                msg2 VARCHAR(250),
                dte DATE,
                tmm DATETIME,
                `show` VARCHAR(25), 
                comm VARCHAR(125),
                serc VARCHAR(5)
            );
            """
            mycursor.execute(myquery1)

            # Second table creation query
            myquery2 = """
            CREATE TABLE IF NOT EXISTS namev (
                ID INT(6) AUTO_INCREMENT PRIMARY KEY NOT NULL,
                namv VARCHAR(100),
                mobv VARCHAR(20),
                comm VARCHAR(200),
                ccode INT(6),
                dtdt DATETIME
            );
            """
            mycursor.execute(myquery2)

            messagebox.showinfo("Success", "Tables 'msgg' and 'namev' created successfully.")
    except Error as e:
        messagebox.showerror("Error", f"Error creating table: {e}")
    finally:
        # Check if 'mycursor' and 'conn' exist and close them if they are open
        if 'mycursor' in locals():
            mycursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


currentDate = datetime.now().strftime('%Y-%m-%d')
currentDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def insert_mess():
    try:
        # Connect to MySQL server and specify the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="vardhmann"
        )
        if conn.is_connected():
            mycursor = conn.cursor()

            # Insert Message query
            insert_query = """
            INSERT INTO msgg (idn, msg, msg2, dte, tmm, `show`, comm, serc)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Data to be inserted
            data = [
                (8, 'msg1sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg1rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg2sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg2rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg3sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg3rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg4sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg4rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg5sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg5rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg6sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg6rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg7rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg7rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg8rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg8rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg9rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg9rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg10rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg10rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg11sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg11rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg12sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg12rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg13sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg13rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg114sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg14rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg15sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg15rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg16sn', '', currentDate, currentDateTime, 'Yes', '', 'sn'),
                (8, 'msg16rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg17rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg17rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg18rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg18rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg19rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
                (8, 'msg19rec', '', currentDate, currentDateTime, 'Yes', '', 'rec'),
            ]

            # Use executemany to insert multiple rows at once
            mycursor.executemany(insert_query, data)
            conn.commit()  # Commit the transaction

            messagebox.showinfo("Success", "Data inserted into 'msgg' successfully.")
    except Error as e:
        messagebox.showerror("Error", f"Error inserting data: {e}")
    finally:
        if 'mycursor' in locals():
            mycursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


def insert_mob():
    try:
        # Connect to MySQL server and specify the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="vardhmann"
        )
        if conn.is_connected():
            mycursor = conn.cursor()

            # Insert Message query
            insert_query = """
            INSERT INTO namev (namv, mobv, comm, ccode, dtdt)
            VALUES (%s, %s, %s, %s, %s)
            """
            
            # Data to be inserted
            data = [
                ('Chitransh', '9784323075', 1,1,''),
                ('Chitransh', '6654882244', 1,1,''),
                ('Chirag', '7879294846', 1,1,''),
                ('Awdhesh', '6484016177', 1,1,''),
                ('Harsh', '9888510025', 1,1,''),
                ('aastha', '9878521446', 1,1,''),
                ('Aditi', '6899289841', 1,1,''),
                ('Charinee', '8989294848', 1,1,''),
                ('Jaishree', '6899289841', 1,1,''),
                ('Ayushi', '8989294848', 1,1,''),
                ('Chandan', '7899289841', 1,1,''),
                ('Adarsh', '8989294848', 1,1,''),
                ('Anurag', '6899289846', 1,1,''),
                ('Yuraj', '9899289846', 1,1,''),
                ('Aman', '6879294841', 1,1,''),
                ('Uday', '8989284848', 1,1,''),
                ('Abhay', '7879294846', 1,1,''),
                ('Yash', '6899289846', 1,1,''),
            ]

            # Use executemany to insert multiple rows at once
            mycursor.executemany(insert_query, data)
            conn.commit()  # Commit the transaction

            messagebox.showinfo("Success", "Data inserted into 'msgg' successfully.")
    except Error as e:
        messagebox.showerror("Error", f"Error inserting data: {e}")
    finally:
        if 'mycursor' in locals():
            mycursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

# Create buttons to trigger database and table creation functions

dbbtn = Button(root, text="Create Database", command=create_database)
dbbtn.place(x=30, y=15, width=130)
dtblbel = Label(root, text="Step 1")
dtblbel.place(x=180, y=15)

tblebtn = Button(root, text="Create Table", command=create_table)
tblebtn.place(x=30, y=65, width=130)
tbllbel = Label(root, text="Step 2")
tbllbel.place(x=180, y=65)

messbtn = Button(root, text="Insert Some Message", command=insert_mess)
messbtn.place(x=30, y=115, width=130)
messlbel = Label(root, text="Step 3")
messlbel.place(x=180, y=115)

mobbtn = Button(root, text="Insert Mob No.& Name", command=insert_mob)
mobbtn.place(x=30, y=165, width=130)
moblbel = Label(root, text="Step 4")
moblbel.place(x=180, y=165)


# Delete buttons to trigger database deletion functions
mobbtn = Button(root, text="Dlete Databse", command=delete_database)
mobbtn.place(x=30, y=215, width=130)
moblbel = Label(root, text="(Optional)")
moblbel.place(x=180, y=215)


# Start the Tkinter event loop
root.mainloop()
