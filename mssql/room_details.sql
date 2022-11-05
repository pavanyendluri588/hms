CREATE TABLE rooms_details (
  room_ID int NOT NULL,
  room_floor int NOT NULL,
  room_no int NOT NULL,
  rooms_status varchar(40) NOT NULL,
  booked_person_id int DEFAULT NULL,
  PRIMARY KEY (room_ID),
  CONSTRAINT rooms_details_ibfk_1 FOREIGN KEY (booked_person_id) REFERENCES dbo.patient_details (id)
) 