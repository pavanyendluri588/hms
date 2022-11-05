CREATE TABLE patient_queue (
  patient_id int NOT NULL DEFAULT '1',
  queue_type varchar(40) NOT NULL DEFAULT 'None',
  queue_status varchar(40) NOT NULL DEFAULT 'None',
  reason varchar(40) NOT NULL DEFAULT 'None',
  doctor_id int NOT NULL DEFAULT '1',
  PRIMARY KEY (patient_id))