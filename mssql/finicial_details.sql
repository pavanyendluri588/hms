CREATE TABLE finance_details (
  finance_id int NOT NULL IDENTITY(1,1) ,
  patient_id int DEFAULT NULL,
  department varchar(100) NOT NULL,
  reason1 varchar(100) NOT NULL,
  Debit int NOT NULL DEFAULT '0',
  credit int NOT NULL DEFAULT '0',
  type_of_charge varchar(45) NOT NULL DEFAULT 'null',
  PRIMARY KEY (finance_id),
 
  CONSTRAINT finance_details_ibfk_1 FOREIGN KEY (patient_id) REFERENCES dbo.patient_details (id),
  CONSTRAINT finance_details_chk_1 CHECK (((Debit >= 0) and (credit >= 0)))
) 