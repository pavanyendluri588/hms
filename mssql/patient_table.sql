CREATE TABLE patient_details (
  id int NOT NULL IDENTITY(100,1),
  name varchar(100) NOT NULL,
  mname varchar(100) DEFAULT NULL,
  lname varchar(40) DEFAULT NULL,
  dob varchar(200) NOT NULL DEFAULT '1990-10-25',
  bloodgroup varchar(20) DEFAULT NULL,
  phone_number bigint NOT NULL DEFAULT '1234567890',
  phone_number2 bigint NOT NULL DEFAULT '1234567890',
  age int DEFAULT NULL,
  gender varchar(30) DEFAULT NULL,
  address varchar(50) DEFAULT NULL,
  city varchar(50) DEFAULT NULL,
  emailid varchar(50) DEFAULT NULL,
  PRIMARY KEY (id)
)