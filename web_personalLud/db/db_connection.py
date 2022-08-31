from ast import Return
import pymysql

def get_connection():
    connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='web_personal',
                                    cursorclass=pymysql.cursors.DictCursor)

    return connection                                       