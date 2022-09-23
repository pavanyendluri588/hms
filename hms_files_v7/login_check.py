import re
import mysql.connector
mydb = None
mycursor=None
#host_nameNone
#user_name=None
#password=None
#database_name=None

mydb = mysql.connector.connect(host='localhost',user='root',passwd='1234',database='hms')
def server_connection(host_name=None,user_name=None,password=None):
     try:
          global mydb
          mydb = mysql.connector.connect(host=host_name,user=user_name,passwd=password)
          print("MYSQL server connection id successfull")
     except Exception as e:
          print("MYSQL server connection is failed\n error is ",e)

def database_connection(host_name=None,user_name=None,password=None,database_name=None):
     try:
         global mydb
         mydb = mysql.connector.connect(host=host_name,user=user_name,passwd=password,database=database_name)
         print(database_name," database connection is successfull")
     except Exception as e:
          print("the database connection is failed\n error is ",e)
        

def execute_cmd(connection,command):
    try:
        global mycursor
        mycursor = connection.cursor()
        mycursor.execute(command)
        print(command," executed successfully")
    except Exception as e:
        print("execution was failed\n error is ",e)

def  create_table(connection,sql_table_statement=None,table_name=None):
   mycursor1 =None
   try:
      database_connection(host_name='localhost',user_name='root',password='1234',database_name='hms')
      #execute(mydb,sql_table_statement)
      mycursor1 = connection.cursor()
      mycursor1.execute(sql_table_statement);
      print(table_name," table is created successfully\n",table_name," table schema : \n",sql_table_statement)
   except Exception as e:
      print(table_name," table is creation is failed due to error:",e)
      
      

server_connection(host_name='localhost',user_name='root',password='1234')
execute_cmd(mydb,"select user,host from mysql.user")
database_connection(host_name='localhost',user_name='root',password='1234',database_name='hms')

login_table_schema = '''CREATE TABLE IF NOT EXISTS login_details(
                         username_hms varchar(45) NOT NULL,
                         password_hms varchar(45) NOT NULL,
                         PRIMARY KEY(username_hms)
                         )'''
create_table(mydb,login_table_schema,"login_table")


def username_password_check(connection,role,username11,password11):
    result=None
    check=None
    try:
        mycursor_upc= connection.cursor()
        mycursor_upc.execute("select * from login_details")
        result = mycursor_upc.fetchall()
        print("result shape:",len(result))
        for a,i,j in result:
            print(a,i,j)
            if a==role and i==username11 and j==password11:

                check=1
        if check == 1:
            print(role,username11,password11," are matched")
            return 'true'
        else:
            print("ROLE:",role,"USERNAME:",username11," PASSWORD:",password11," are not matched")
            return 'false'

    except Exception as e:
        print("username_password_check function:",e)
        return 'false'
    

def get_execution_result(command):
    global mydb
    result=None
    check=None
    execution_cursor = mydb.cursor()
    print("Exexition in database:",command)
    execution_cursor.execute(command)
    result = execution_cursor.fetchall()
    
    mydb.commit()
    print("result:",result)
    return result
    
data = get_execution_result("select * from rooms_details")
print(data)
    
"""
role_ch="Doctor"
username_ch="pavanyendluri588"
password_ch="Pavan@99499"

ch1 = username_password_check(mydb,role_ch,username_ch,password_ch)
if ch1 == 'true':
    print(username_ch,password_ch," are matched")
else:
    print("USERNAME:",username_ch," PASSWORD:",password_ch," are not matched")
    
"""
