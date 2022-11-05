CREATE TABLE login_details (
  user_role varchar(45) NOT NULL,
  user_name varchar(45) NOT NULL unique,
  password varchar(45) NOT NULL,
) 