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

