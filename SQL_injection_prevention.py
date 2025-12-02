from urllib import request
import mysql.connector
import os


    
"""Retrieving credientals to connect to my SQL"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",        
  password="Testing123",  
  database="Bike Store Dataset"
)

print(mydb)
my_cursor = mydb.cursor()

def vulnerable(Cursor,user_input):
    
    vulnerable_query = "SELECT * FROM users WHERE username = " + user_input
    
    print(f"\n[VULNERABLE] Testing input: {user_input}")
    print(f"SQL Executed: {vulnerable_query}")
    
    
    try:
        Cursor.execute(vulnerable_query)
      
        if Cursor.fetchone():
            print("Failed: SQL Injection was succesful and access has been granted")
            return True
        else:
            print("Input has been blocked")
            return False
    except Exception as e:
        print(f"There was an error during execution. Please read for more info:{e}")
        return False
    

def check_secure(Cursor, user_input):
  
    secure_query = "SELECT * FROM users WHERE username = %s"
    
    print(f"\n[SECURE] Testing input: {user_input}")
    
    try:
      
        Cursor.execute(secure_query, (user_input,)) 
        if Cursor.fetchone():
            print("Benign input was able to connect")
            return True
        else:
            print("Harmful input was blocked")
            return False
    except Exception as e:
        print(f"There was an error during execution. Please read for more info: {e}")
        return False
    
 
PAYLOAD_MALICIOUS = "' OR 1=1 --"
PAYLOAD_BENIGN = "testuser"

print("\nFirst Audit: ")
vulnerable_result = vulnerable(my_cursor, PAYLOAD_MALICIOUS)

if vulnerable_result:
    print("\nVulnerability Status: Sucessful bypass | High risk")
    
    print("\Second Audit:")

secure_result = check_secure(my_cursor, PAYLOAD_MALICIOUS)

if not secure_result:
    print("\n Status: Secure | Attack was blocked and queries were validated :)")
    
    