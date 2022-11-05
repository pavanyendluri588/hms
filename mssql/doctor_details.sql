CREATE TABLE doctor_details (
  doctor_id int NOT NULL IDENTITY(1,1) ,
  doctor_name varchar(100) NOT NULL DEFAULT 'None',
  doctor_age int DEFAULT '0',
  doctor_address varchar(100) DEFAULT 'None',
  doctor_phone_number int NOT NULL DEFAULT '0',
  doctor_qualification varchar(100) DEFAULT 'None',
  PRIMARY KEY (doctor_id));