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

