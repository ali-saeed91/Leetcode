# Write your MySQL query statement below
SELECT name
FROM Customer as a
WHERE NOT a.referee_id = 2 OR a.referee_id is NULL