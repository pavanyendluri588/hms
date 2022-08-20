import mysql.connector
mydb=None
mycursor=None
#host_nameNone
#user_name=None
#password=None
#database_name=None


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

server_connection('hms_user','localhost','Pavan@99499')
database_connection('hms_user','localhost','1234','Pavan@99499')