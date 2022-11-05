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
        "Database=hms;"
        "Trusted_Connection=yes;" 
    )
          print("MYSQL server connection id successfull")
     except Exception as e:
          print("MYSQL server connection is failed\n error is ",e)


   
mydb = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-KCCDBPE\SQLEXPRESS;"
        "Database=hms;"
        "Trusted_Connection=yes;" 
    )
def server_connection(host_name=None,user_name=None,password=None):
     try:
          global mydb
          mydb = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-KCCDBPE\SQLEXPRESS;"
        "Database=hms;"
        "Trusted_Connection=yes;" 
    )
          print("MYSQL server connection id successfull")
     except Exception as e:
          print("MYSQL server connection is failed\n error is ",e)

def database_connection(host_name=None,user_name=None,password=None,database_name=None):
     try:
         global mydb
         mydb = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-KCCDBPE\SQLEXPRESS;"
        "Database=hms;"
        "Trusted_Connection=yes;" 
    )
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


      
      

server_connection(host_name='localhost',user_name='root',password='1234')
execute_cmd(mydb,"select * from hms.atient_details")
database_connection(host_name='localhost',user_name='root',password='1234',database_name='hms')




def username_password_check(connection,role,username11,password11):
    result=None
    check=None
    try:
        
        result=get_execution_result("select * from hms.login_details")
    
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
    if 'select' in command:
          execution_cursor = mydb.cursor()
          print("Exexition in database:",command)
          execution_cursor.execute(command)
          result = execution_cursor.fetchall()
    
          mydb.commit()
          print("result:",result)
          return result
    else:
          execution_cursor = mydb.cursor()
          print("Exexition in database:",command)
          execution_cursor.execute(command)
          
    
          mydb.commit()   
          print("result:",result)
          return []
    
data = get_execution_result("select * from hms.rooms_details")
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
