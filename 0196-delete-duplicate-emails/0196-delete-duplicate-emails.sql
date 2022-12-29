# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE a FROM Person as a, Person as b
WHERE a.email = b.email AND a.id > b.id
