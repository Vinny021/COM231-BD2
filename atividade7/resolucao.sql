-- === Alunos ===
-- João Pedro M. de Sousa - 2018006008
-- Vinícius Barbosa - 2020009867


	-- Exercício 1

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
	department varchar(100),
	diplomas type_diplomas[],
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

CREATE TABLE prerequisite (
	courseNo varchar(50) not null,
	isPrerequisite varchar(50)[],
	hasPrerequisite varchar(50)[]
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

-- === Alunos ===
-- João Pedro M. de Sousa - 2018006008
-- Vinícius Barbosa - 2020009867

    -- Exercício 2

-- 1
INSERT INTO person
    (ssn, name, birthDate, address, telephones)
VALUES 
    (123456789, ROW('Russo', 'Renato'), '1980-01-01', ROW('Rua A', 22, 'São Paulo', 1000, 'Brasil'), '{12345, 54321}');

-- 2
INSERT INTO student
    (ssn, name, birthDate, address, studentNo, department) 
VALUES 
    (123123123, ROW('Leite', 'Claudia'), '1985-05-01', ROW('Rua B', 14, 'São Paulo', 1000, 'Brasil'), 999, 'Departamento 02 - Ciência da Computação' );

-- 3
INSERT INTO student
    (ssn, name, birthDate, address, studentNo, department) 
VALUES 
    (111222333, ROW('Raia', 'Claudia'), '1965-12-12', ROW('Rua D', 1, 'Rio de Janeiro', 2000, 'Brasil'), 888, 'Departamento 02 - Ciência da Computação' );

-- 4
INSERT INTO student
    (ssn, name, birthDate, address, studentNo, department) 
VALUES 
    (333222111, ROW('Prado', 'Osmar'), '1975-06-04', ROW('Rua das Palmeiras', 99, 'Vitoria', 3000, 'Brasil'), 777, 'Departamento 02 - Ciência da Computação' );

-- 5
INSERT INTO professor
    (ssn, name, birthDate, address, profNo, bankaccount) 
VALUES 
    (666999666, ROW('Bonifacio', 'Jose'), '1984-11-22', ROW('Rua K', 5, 'Rio de Janeiro', 2000, 'Brasil'), 777, ROW('310123456789', 'ING'));

-- 6
INSERT INTO 
    professor(ssn, name, birthDate, address, telephones,profNo, bankaccount) 
VALUES 
    (987987987, ROW('Madalena', 'Maria'), '1930-05-31', ROW('Rua K', 15, 'Rio de Janeiro', 2000, 'Brasil'), '{2222}',666, ROW('33333333', 'ING'));

-- 7
UPDATE student 
    SET telephones = '{2222, 3333}' 
    WHERE (name).lastName = 'Leite' AND (name).firstName = 'Claudia';

-- 8
UPDATE student 
    SET telephones = (SELECT telephones FROM person WHERE (name).lastName = 'Russo' AND (name).firstName = 'Renato') 
    WHERE (name).lastName = 'Raia' AND (name).firstName = 'Claudia'

-- 9
INSERT INTO course 
    (courseNo, courseName, credits, year, department, teacher) 
VALUES
    ('INFO-H-415', 'Bancos de Dados Avançados', 5, 4, 'Departamento 2 -  Ciência da Computação', 987987987);

-- 10
INSERT INTO course 
    (courseNo, courseName, credits, year, department, teacher) 
VALUES 
    ('INFO-H-888', 'Data Mining', 5, 5, 'Departamento 2 - Ciência da Computação', 666999666);

INSERT INTO prerequisite
    (courseNo, isPrerequisite, hasPrerequisite)
VALUES
    ('INFO-H-888', '{}', '{INFO-H-415}');

-- 11
INSERT INTO course 
    (courseNo, courseName, credits, year, department, teacher) 
VALUES 
    ('INFO-H-999', 'Data Warehouse', 5, 5, 'Departamento 2 - Ciência da Computação', 666999666);

-- 12
INSERT INTO hasTaken
    (courseNo, studentNo, year, grades)
VALUES
    ('INFO-H-415', 123123123, 2010, '{18, 19}');

-- 13 
INSERT INTO enrolls
    (studentNo, courseNo)
VALUES
    (123123123, 'INFO-H-888');

-- 14
INSERT INTO enrolls
    (studentNo, courseNo)
VALUES
    (123123123, 'INFO-H-999');

-- 15
INSERT INTO enrolls
    (studentNo, courseNo)
VALUES
    (123456789, 'INFO-H-888');

INSERT INTO enrolls
    (studentNo, courseNo)
VALUES
    (123456789, 'INFO-H-999');

-- 16
INSERT INTO enrolls
    (studentNo, courseNo)
VALUES
    (111222333, 'INFO-H-888');

-- === Alunos ===
-- João Pedro M. de Sousa - 2018006008
-- Vinícius Barbosa - 2020009867

    -- Exercício 3

-- 1
SELECT 
    (name).firstName, (name).lastName 
FROM 
    person;

-- 2
SELECT 
    (name).firstName, (name).lastName, ssn 
FROM 
    student;

-- 3
SELECT 
    (p.name).firstName, (p.name).lastName
FROM 
    person AS p
LEFT JOIN student ON student.ssn = p.ssn
LEFT JOIN professor ON professor.ssn = p.ssn
WHERE 
    student.ssn IS NULL
AND 
    professor.ssn IS NULL;

-- 4
SELECT 
    (name).firstName, (name).lastName, address 
FROM 
    person 
WHERE 
    ssn = 123456789;

-- 5
SELECT 
    telephones FROM student 
WHERE 
    (name).firstName = 'Claudia' AND (name).lastName = 'Leite';

-- 6
SELECT 
    (name).firstName, (name).lastName 
FROM 
    person 
WHERE 
    telephones[1] = '2222';

-- 7
SELECT 
    (name).firstName, (name).lastName 
FROM 
    person 
WHERE 
    telephones[1] IS NULL;

-- 8
SELECT 
    courseno
FROM 
    enrolls
WHERE 
    studentno = 123123123;

-- 9

