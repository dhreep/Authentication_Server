from wed_db_functions import create_table, insert_table, update_login, verify_password, verify_username, verify_initiator
from wed_db_functions import retrieve_listener_details_auth_key, retrieve_listener_details_username, update_logout,display_table
import sqlite3
from hashing_db import getKey,encryptToStore,decryptFromStore
import uuid

def main():
    # print("Testing")
    # key = getKey()
    # print(key)
    # plain = "Dhruv"
    # enc = encryptToStore(key=key,plaintext=plain)
    # print(enc)
    # plain = "Dhruv"
    # enc = encryptToStore(key=key,plaintext=plain)
    # print(enc)
    # key = getKey()
    # print(key)
    # plain = decryptFromStore(key=key,enctext=enc)
    # print(plain)
    conn_db = sqlite3.connect("Servdata.sqlite",check_same_thread=False)
    cursor = conn_db.cursor()
    create_table(cursor=cursor,conn=conn_db)
    insert_table(cursor=cursor,conn=conn_db,username="Lakshay",pwd="Bajaj",ip="235.24.26.27")
    insert_table(cursor=cursor,conn=conn_db,username="Dhruv",pwd="Bajaj",ip="245.24.26.27")
    update_login(cursor=cursor,conn=conn_db,auth_key="645",port=10305,username="Dhruv")
    update_login(cursor=cursor,conn=conn_db,auth_key="789",port=10306,username="Lakshay")
    conn_db.commit()
    display_table(cursor=cursor)
    


if __name__ == "__main__":
    main()