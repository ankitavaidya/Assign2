Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import mysql.connector

from mysql.connector import Error

from mysql.connector import errorcode

def insertInTable(username,password):
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='sample',
                             user='root',
                             password='root')
        cursor = connection.cursor(prepared=True)
        sql_insert_query = """ INSERT INTO `register`
                          (`username`, `password`) VALUES (%s,%s)"""
        insert_tuple = (username, password)
        result  = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print ("Record inserted successfully into python_users table")
        return render_template('login.html')
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
