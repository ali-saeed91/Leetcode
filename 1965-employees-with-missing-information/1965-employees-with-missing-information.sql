# Write your MySQL query statement below
SELECT a.employee_id
FROM Employees as a
LEFT JOIN Salaries as b
ON a.employee_id = b.employee_id
WHERE b.salary IS NULL
UNION
SELECT b.employee_id
FROM Employees as a
RIGHT JOIN Salaries as b
ON a.employee_id = b.employee_id
WHERE a.name IS NULL
ORDER BY employee_id
