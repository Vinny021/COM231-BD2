CREATE TYPE type_name as (
	lastName VARCHAR(20),
	firstName VARCHAR(20)
);

CREATE TYPE type_address as (
	street varchar(40),
	number int, 
	city varchar(20),
	zip int,
	country varchar(20)
);

CREATE TABLE person (
	ssn int not null,
	name type_name,
	birthDate date,
	address type_address,
	telephones int[],
	PRIMARY KEY (ssn)
);

CREATE TYPE type_diplomas as (
	name varchar(20),
	year int
);

CREATE TABLE student (
	studentNo int not null,
	department varchar(20),
	diplomas type_diplomas[] NOT NULL,
	PRIMARY KEY(studentNo)
) INHERITS (person);

create table hasTaken(
	courseNo varchar(50),
	studentNo int,
	year int,
	grades int[]
);

CREATE TABLE enrolls (
	studentNo int,
	courseNo varchar(50)
);

CREATE TABLE course (
	courseNo varchar(50) not null,
	courseName varchar(100) NOT NULL,
	credits int,
	year int,
	department varchar(100),
	teacher int, 
	PRIMARY KEY(courseNo)
);

CREATE TYPE type_bankAccount as (
	number varchar(30),
	bank varchar(20)
);

CREATE TABLE professor (
	profNo int not null,
	bankAccount type_bankAccount,
	PRIMARY KEY (profNo)
) INHERITS (person);

