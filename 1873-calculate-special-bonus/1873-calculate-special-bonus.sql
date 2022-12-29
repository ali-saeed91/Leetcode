# Write your MySQL query statement below
SELECT employee_id, (salary*(employee_id %2)*(name NOT LIKE "M%")) as bonus
FROM Employees as e
ORDER BY e.employee_id