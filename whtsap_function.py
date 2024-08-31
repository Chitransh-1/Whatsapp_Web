from tkinter import *
import mysql.connector
from datetime import datetime


def insert_into_msg(detta):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vardhmann"
    )
    mycursor = conn.cursor()
    myquery = "INSERT INTO msgg (idn, msg, msg2, dte, tmm, `show`, comm, serc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        mycursor.execute(myquery, detta)
        conn.commit()
        print("Inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mycursor.close()
        conn.close()


def get_detaa():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vardhmann"
    )
    mycursor = conn.cursor()
    qurry = "SELECT ID, namv, mobv, dtdt FROM namev ORDER BY dtdt DESC"
    try:
        mycursor.execute(qurry)
        detaa = mycursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        detaa = []
    finally:
        mycursor.close()
        conn.close()
    return detaa


def get_msgg(idnv):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vardhmann"
    )
    mycursor = conn.cursor()
    myqurry = f"SELECT * FROM msgg WHERE idn = '{idnv}'"
    try:
        mycursor.execute(myqurry)
        detaa = mycursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        detaa = []
    finally:
        mycursor.close()
        conn.close()
    return detaa


def get_name(idnv):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vardhmann"
    )
    mycursor = conn.cursor()
    myqurry = f"SELECT namv, mobv FROM namev WHERE ID = '{idnv}'"
    try:
        mycursor.execute(myqurry)
        detaa = mycursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        detaa = []
    finally:
        mycursor.close()
        conn.close()
    return detaa
    

currentDate = datetime.now().strftime('%Y-%m-%d')
currentDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def insert_msg(deta, idid, timee):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vardhmann"
    )
    mycursor = conn.cursor()

    idn = idid
    print(idn)
    msg_value = deta
    msg2 = ""
    dtte = currentDate
    dettime = currentDateTime
    showw = "yes"
    conm = ""
    serc_value = "sn"

    insert_query = """
    INSERT INTO msgg (idn, msg, msg2, dte, tmm, `show`, comm, serc) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    update_query = """
    UPDATE namev
    SET dtdt = %s
    WHERE ID = %s
    """

    dtte_value = timee
    idid_value = idid 

    try:
        mycursor.execute(insert_query, (idn, msg_value, msg2, dtte, dettime, showw, conm, serc_value))
        
        mycursor.execute(update_query, (dtte_value, idid_value))
        
        conn.commit()
        print("Message inserted and date updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mycursor.close()
        conn.close()