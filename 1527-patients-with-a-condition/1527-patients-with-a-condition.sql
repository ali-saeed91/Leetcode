# Write your MySQL query statement below
SELECT *
FROM Patients as result
WHERE result.conditions LIKE "% DIAB1%" OR result.conditions LIKE "DIAB1%"