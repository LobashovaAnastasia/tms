sudo -i -u postgres

psql

CREATE DATABASE Homework14

\c homework14;


CREATE TABLE STUDENTS(
 id serial PRIMARY KEY,
 name VARCHAR(20) NOT NULL,
 age INTEGER NOT NULL,
 programming_language VARCHAR(6) NOT NULL
);


CREATE TABLE AUDIENCES(
 number INTEGER NOT NULL,
 teacher VARCHAR(20) NOT NULL,
 floor INTEGER NOT NULL,
 programming_language VARCHAR(20) NOT NULL,
 student_id INTEGER,
 FOREIGN KEY (student_id)
  REFERENCES STUDENTS (id)
   ON DELETE CASCADE ON UPDATE NO ACTION
);


INSERT INTO STUDENTS (name, age, programming_language)
VALUES
  ('Alex', 34, 'Python'),
  ('Ann', 32, 'Python'),
  ('Kate', 25, 'C++'),
  ('Mark', 20, 'C++'),
  ('Olivia', 29, 'Java'),
  ('Sophia', 25, 'Java');


INSERT INTO AUDIENCES (number, teacher, floor, programming_language)
VALUES
  (332, 'Alex', 3, 'Python'),
  (415, 'Ivan', 4, 'C++'),
  (111, 'Mark', 1, 'Java');
