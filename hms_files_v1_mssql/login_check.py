import pyodbc
#driver='{SQL Server Native Client 11.0}'
pyodbc.drivers()
#connecting to database
mydb = None
mycursor=None



def server_connection():
     try:
          global mydb
          mydb=pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-KCCDBPE\SQLEXPRESS;"
        "Database=library_management;"
        "Trusted_Connection=yes;" 
    )
          print("MYSQL server connection id successfull")
     except Exception as e:
          print("MYSQL server connection is failed\n error is ",e)


        

def execute_cmd(connection,command):
    try:
        global mycursor
        server_connection()
        mycursor = connection.cursor()
        mycursor.execute(command)
        print(command," executed successfully")
    except Exception as e:
        print("execution was failed\n error is ",e)

      
      

server_connection()
execute_cmd(mydb,"select * from login_details")


login_table_schema = '''CREATE TABLE IF NOT EXISTS login_details(
                         username_hms varchar(45) NOT NULL,
                         password_hms varchar(45) NOT NULL,
                         PRIMARY KEY(username_hms)
                         )'''



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
